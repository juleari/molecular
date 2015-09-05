var server  = require("./modules/server"),
    urls    = require("./urls"),
    views   = require("./views"),
    posts   = require("./posts"),
    v_files = require("./views_files");

var handle  = {},
    postH   = ["mol2"],
    files   = ["stat"];

for (var i = postH.length; i--; ) {
    handle[ "/" + postH[i] ] = posts[ postH[i] ];
}

for (var i = files.length; i--; ) {
    handle[ "/" + files[i] ] = v_files[ files[i] ];
}

handle["/"] = views.init;

server.start(urls.route, handle);