__author__ = 'Nathan Meadows'

from cgi import escape
from py.tag import Tag
from py.db import DB


class Urls:

    def __init__(self):
        pass

    @staticmethod
    def wrapTemplate(content):
        sitetags = Tag('site')
        header = open('negativenull.com/views/header.html').read()
        header = sitetags.processTags(header)

        footer = open('negativenull.com/views/footer.html').read()
        footer = sitetags.processTags(footer)

        return header+content+footer

    @staticmethod
    def index(environ, start_response):
        cont = (open('negativenull.com/views/index.html').read())
        pagetags = Tag('tag')
        return [Urls.wrapTemplate(pagetags.processTags(cont))]

    @staticmethod
    def hello(environ, start_response):
        args = environ['myapp.url_args']
        if args:
            subject = escape(args[0])
        else:
            subject = 'World'
        return ['''Hello %(subject)s
                Hello %(subject)s!
                ''' % {'subject': subject}]

    @staticmethod
    def page(environ, start_response):

        args = environ['myapp.url_args']
        if args:
            pageid = escape(args[0])
            db = DB()
            page = db.query("select * from pages where id=%s" % pageid, returnone=True)

        else:
            return Urls.not_found

        return [page['content']]

    @staticmethod
    def not_found(environ, start_response):
        cont = (open('negativenull.com/views/404.html').read())
        return [cont]

