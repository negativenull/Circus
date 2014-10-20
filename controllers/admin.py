__author__ = 'Nathan Meadows'

from cgi import escape
from py.environment import *


class Admin(Urls):

    @staticmethod
    def index(environ, start_response):
        from py.environment import Env

        tables = Env.db.gettables()
        content = '<h1>Database tables</h1><ul>'
        for table in tables:
            content += "<li>%s</li>" % table['table_name']
        content += "</ul>"

        return Urls.wrapTemplate(content)

