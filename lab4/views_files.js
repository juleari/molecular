var fs   = require("fs");

function stat(response, path, type) {
  
    fs.readFile(__dirname + "/public" + path, "binary", function(error, file) {
        
        if (error) {

            response.writeHead(500, {"Content-Type": "text/plain"});
            response.write(error + "\n");
            response.end();

        } else {

            response.writeHead(200, {"Content-Type": type});
            response.write(file, "binary");
            response.end();
        }
    });
}

exports.stat = stat;