__author__ = 'Nathan Meadows'

from cgi import escape
from py.environment import *


class Page(Urls):

    @staticmethod
    def page(environ, start_response):
        from py.environment import Env

        args = environ['myapp.url_args']
        if args:

            if args[0] == 'add':
                return Page.add(environ, start_response)

            pageid = escape(args[0])
            page = Env.db.query("select * from pages where id=%s" % pageid, returnone=True)
            content = Urls.tag.processTags(page['content'])

        else:
            return Urls.not_found
        return Urls.wrapTemplate(content)

    @staticmethod
    def add(environ, start_response):
        postdata = environ['wsgi.input'].read()  #param1=value1&param2=value2
        import urlparse
        data = urlparse.parse_qs(postdata)

        from py.environment import Env

        content = '<h1>Post data</h1><ul>'
        for k,v in data.iteritems():
            content += "<li>%s = %s</li>" % (k,v[0])
        content += "</ul>"

        return Urls.wrapTemplate(content)
