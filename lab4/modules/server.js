var http = require("http"),
    url  = require("url"),
    func = require("./functions");

var PORT_NUMBER = 3001;

function start(route, handle) {
    
    function if_ok(request, response, pathname) {
  
        var postData = "";
        request.addListener("data", function(postDataChunk) {
          
            postData += postDataChunk;
        });

        request.addListener("end", function(postDataChunk) {

            console.log(postData, postDataChunk, pathname)
            
            route(handle, pathname, response, postData, request.headers['user-agent']);
        });
    }

    function onRequest(request, response) {

        var pathname = url.parse(request.url).pathname,
            style    = /\/css(.*\.css)/,
            js       = /\/js(.*\.js)/,
            img      = /\/img(.*\..*)/;

        request.setEncoding("utf8");

        cookie = func.parseCookies(request);

        if_ok(request, response, pathname);
    }

    http.createServer(onRequest).listen(PORT_NUMBER);
    console.log("Server has started.");
}

exports.start = start;