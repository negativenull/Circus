import sys
sys.path.append('/var/www/Circus/')

import re
from py.environment import *


def application(environ, start_response):

    path = environ.get('PATH_INFO', '').lstrip('/')
    for regex, callback in router:

        match = re.search(regex, path)
        if match is not None:
            environ['myapp.url_args'] = match.groups()
            start_response('200 OK', [('Content-Type', 'text/html')])
            return callback(environ, start_response)

    start_response('404 NOT FOUND', [('Content-Type', 'text/html')])
    return Urls.not_found(environ, start_response)

