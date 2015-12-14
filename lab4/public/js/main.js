var scene = new THREE.Scene();
var camera = new THREE.PerspectiveCamera( 105, window.innerWidth*0.7 / window.innerHeight, 0.1, 1000 );

var renderer = new THREE.WebGLRenderer();
renderer.setSize( window.innerWidth, window.innerHeight );
document.body.appendChild( renderer.domElement );

e = 30;

redraw = function(json_data) {
    scene = new THREE.Scene();

    console.log(json_data)

    scene.children = []

    var geometry, material, sphere,
        spheres = [];

    for (var i = 0; i < json_data.points.length; i++) {

        geometry = new THREE.SphereGeometry(5, 10, 8);
        material = new THREE.MeshBasicMaterial( { color: json_data.points[i].color } );
        sphere   = new THREE.Mesh( geometry, material );
        
        sphere.position.x = json_data.points[i].position[0] * e;
        sphere.position.y = json_data.points[i].position[1] * e;
        sphere.position.z = json_data.points[i].position[2] * e;

        spheres.push(sphere);
        
        scene.add(sphere);
    }

    v0 = new THREE.Vector3(0, 1, 0);

    for (var i = 0; i < json_data.bonds.length; i++) {

        i1 = json_data.bonds[i][0] - 1;
        i2 = json_data.bonds[i][1] - 1;

        v  = new THREE.Vector3 (
            spheres[i2].position.x - spheres[i1].position.x,
            spheres[i2].position.y - spheres[i1].position.y,
            spheres[i2].position.z - spheres[i1].position.z
        )

        vlen = v.length();

        geometry = new THREE.CylinderGeometry(json_data.bonds[i][2], json_data.bonds[i][2], vlen/2);
        material = new THREE.MeshBasicMaterial( { color: json_data.points[i1].color } );
        cylinder = new THREE.Mesh( geometry, material );

        cylinder.position.x = spheres[i1].position.x + v.x / 4;
        cylinder.position.y = spheres[i1].position.y + v.y / 4;
        cylinder.position.z = spheres[i1].position.z + v.z / 4;

        v1 = new THREE.Vector3()
        v2 = new THREE.Vector3()
        v2.crossVectors(v0, v)
        
        v0.normalize()
        v1.copy(v)

        v1.normalize()
        d = v0.dot(v1)

        angle = Math.acos(d)
        axis  = v2.normalize()

        cylinder.quaternion.setFromAxisAngle(axis, angle);

        scene.add(cylinder);

        material = new THREE.MeshBasicMaterial( { color: json_data.points[i2].color } );
        cylinder = new THREE.Mesh( geometry, material );

        cylinder.position.x = spheres[i2].position.x - v.x / 4;
        cylinder.position.y = spheres[i2].position.y - v.y / 4;
        cylinder.position.z = spheres[i2].position.z - v.z / 4;

        cylinder.quaternion.setFromAxisAngle(axis, angle);

        scene.add(cylinder);
    }
}

/*color = [0x8800ff, 0x0088ff, 0x00ff88, 0x88ff00, 0xff0088, 0xff8800, 0xffff00, 0x00ffff];

points = [{
    position : [-2.0968, 0.5166, 0.2632],
    color    : 0xff0000
}, {
    position : [-1.0683, 0.8066, -0.2761],
    color    : 0xaaaaaa
}, {
    position : [0.1064, 1.1376, -0.8919],
    color    : 0xff0000
}, {
    position : [-1.5962, 1.2265, -1.0571],
    color    : 0xffffff
}, {
    position : [0.0939, 1.5813, -1.7172],
    color    : 0xffffff
}];

bonds = [
    [1, 2, 2],
    [2, 3, 1],
    [2, 4, 1],
    [3, 5, 1]
]*/

camera.position.z = 100;

function render() {
    renderer.setSize( window.innerWidth, window.innerHeight );
    camera.aspect = window.innerWidth*0.7 / window.innerHeight;
    camera.updateProjectionMatrix();

    requestAnimationFrame( render );
    renderer.render( scene, camera );
}
render();

var ajax = function() {
    var input = $('select').val() || "O=CO";
      
    $.ajax({
        url: '/mol2',
        type: 'Post',
        data: {name: input},
        success: function(a) {
            j = JSON.parse(a);
            redraw(j);
            $('.current').html( input );
            $('input').val("");
            console.log('success', j, arguments); 
        },
        error: function() {
            console.log('error', arguments); 
        }
    })
}

ajax()

$(document).on('change', 'select', ajax);