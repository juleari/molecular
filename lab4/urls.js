function route(handle, pathname, response, data, user_agent) {
  
    var style = /\/css(.*\.css)/,
        js    = /\/js(.*\.js)/,
        img   = /\/img(.*\..*)/;

    if (data) {

        console.log('post data', data, pathname);
        if (typeof handle[pathname] === 'function') handle[pathname](response, data, user_agent)
        else {
            console.log("No request handler found for " + pathname, data);
            response.writeHead(404, {'Content-Type': 'text/plain'});
            response.write(404);
            response.end();
        }
   
    } else {

        if (typeof handle[pathname] === 'function') {

            handle[pathname](response, user_agent);
            return;
        } else {

            if ((/(.*)_(.*)/).test(pathname) && typeof handle[RegExp.$1] === 'function') {

                handle[RegExp.$1](response, user_agent, RegExp.$2);
                return;
            }
        }
        
        if (style.test(pathname)) {

            handle['/stat'](response, pathname, 'text/css');
            return;
        }

        if (js.test(pathname)) {

            handle['/stat'](response, pathname, 'text/javascript');
            return;
        }              

        if (img.test(pathname)) {

            handle['/stat'](response, pathname, 'image/png');
            return;
        }
    }
  
}

exports.route = route;