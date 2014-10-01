__author__ = 'Nathan Meadows'

from cgi import escape
from py.tag import Tag


class Urls:

    # map urls to functions

    def __init__(self):
        pass

    @staticmethod
    def index(environ, start_response):
        cont = (open('negativenull.com/index.html').read())
        tags = Tag('tag')

        start_response('200 OK', [('Content-Type', 'text/html')])
        return [tags.processTags(cont)]

    @staticmethod
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

    @staticmethod
    def not_found(environ, start_response):
        cont = (open('negativenull.com/404.html').read())
        start_response('404 NOT FOUND', [('Content-Type', 'text/html')])
        return [cont]

