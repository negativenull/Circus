import sys
sys.path.append('../')
sys.path.append('negativenull.com/')


import re
from py.urls import Urls
from py.router import router


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



#old main application
#def applicationbak(environ, start_response):
#    controllers = (open('negativenull.com/index.html').read())
#    tags = Tag('tag')
#
#
#    start_response('200 OK', [('Content-Type', 'text/html')])
#    return [tags.processTags(controllers)]