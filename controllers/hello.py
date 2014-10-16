__author__ = 'nathan'

from cgi import escape
from py.environment import *


class Hello(Urls):

    @staticmethod
    def hello(environ, start_response):
        args = environ['myapp.url_args']
        if args:
            subject = escape(args[0])
        else:
            subject = 'World'

        return Urls.wrapTemplate('''Hello %(subject)s
                Hello %(subject)s!
                ''' % {'subject': subject})