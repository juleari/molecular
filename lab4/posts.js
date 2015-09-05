var fs   = require("fs");

COLORS = {
    "O" : 0xff0000,
    "H" : 0xffffff,
    "C" : 0xaaaaaa,
    "Cl": 0x00ff00,
    "F" : 0x009911,
}

function mol2(response, data) {
    var name = data.split("=")[1],
        pts  = [],
        bnds = [];

    console.log(data, name)

    fs.readFile(__dirname + "/public/mol2/" + decodeURIComponent(name) + ".mol2", 'utf8', function(error, file) {
        
        if (error) {

            response.writeHead(500, {"Content-Type": "text/plain"});
            response.write(error + "\n");
            response.end();

        } else {

            console.log(file);

            counts = file.split("\n")[2].split(" ");

            col_atoms = counts[counts.length - 5]
            col_bonds = counts[counts.length - 4]        

            atoms_strings = file.split("@<TRIPOS>ATOM\n")[1].split("\n");

            for (i = 0; i < col_atoms; i++) {
                atom_string = atoms_strings[i].split(/ +/);

                pts.push({
                    position: [atom_string[3], atom_string[4], atom_string[5]],
                    color   : COLORS[ atom_string[2] ]
                });

                console.log(pts[i])
            }        

            bonds_strings = file.split("@<TRIPOS>BOND\n")[1].split("\n");

            for (i = 0; i < col_bonds; i++) {
                bond_string = bonds_strings[i].split(/ +/);

                bnds.push([bond_string[2], bond_string[3], bond_string[4]]);

                console.log(bnds[i])
            };

            response.writeHead(200, {"Content-Type": "text/plain"});
            response.write(JSON.stringify({points: pts, bonds: bnds}), "utf8");
            response.end();
        }
    });
}

exports.mol2 = mol2;