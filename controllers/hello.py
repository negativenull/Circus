__author__ = 'nathan'

from cgi import escape
from py.tag import Tag
from py.db import DB
from py.urls import Urls


class Hello(Urls):

    @staticmethod
    def hello(environ, start_response):
        args = environ['myapp.url_args']
        if args:
            subject = escape(args[0])
        else:
            subject = 'World'

        return [Urls.wrapTemplate('''Hello %(subject)s
                Hello %(subject)s!
                ''' % {'subject': subject})]