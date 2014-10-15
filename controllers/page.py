__author__ = 'Nathan Meadows'

from cgi import escape
from py.environment import Env, Urls



class Page(Urls):

    @staticmethod
    def page(environ, start_response):

        args = environ['myapp.url_args']
        if args:
            pageid = escape(args[0])
            page = Env.db.query("select * from pages where id=%s" % pageid, returnone=True)
            content = Urls.tag.processTags(page['content'])

        else:
            return Urls.not_found

        return [Urls.wrapTemplate(content)]

