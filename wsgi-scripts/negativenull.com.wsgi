import sys
sys.path.append('../')
sys.path.append('negativenull.com/')
from py.functions import Functions
from py.tag import Tag
import re
from cgi import escape

def index(environ, start_response):
    cont = (open('negativenull.com/index.html').read())
    tags = Tag('tag')


    start_response('200 OK', [('Content-Type', 'text/html')])
    return [tags.processTags(cont)]


def hello(environ, start_response):
    args = environ['myapp.url_args']
    if args:
        subject = escape(args[0])
    else:
        subject = 'World'
    start_response('200 OK', [('Content-Type', 'text/html')])
    return ['''Hello %(subject)s
            Hello %(subject)s!

''' % {'subject': subject}]


def not_found(environ, start_response):
    cont = (open('negativenull.com/404.html').read())
    start_response('404 NOT FOUND', [('Content-Type', 'text/html')])
    return [cont]

# map urls to functions
urls = [
    (r'^$', index),
    (r'hello/?$', hello),
    (r'hello/(.+)$', hello)
]


def application(environ, start_response):

    path = environ.get('PATH_INFO', '').lstrip('/')
    for regex, callback in urls:
        match = re.search(regex, path)
        if match is not None:
            environ['myapp.url_args'] = match.groups()
            return callback(environ, start_response)
    return not_found(environ, start_response)


#old main application
def applicationbak(environ, start_response):
    cont = (open('negativenull.com/index.html').read())
    tags = Tag('tag')


    start_response('200 OK', [('Content-Type', 'text/html')])
    return [tags.processTags(cont)]