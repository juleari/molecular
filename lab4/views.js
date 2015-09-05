var fs   = require("fs");

function init (response) {

    fs.readFile(__dirname + "/public/index.html", "binary", function(error, file) {
        
        if (error) {

            response.writeHead(500, {"Content-Type": "text/plain"});
            response.write(error + "\n");
            response.end();

        } else {

            response.writeHead(200, {"Content-Type": "text/html"});
            response.write(file, "binary");
            response.end();
        }
    });

}

exports.init = init;