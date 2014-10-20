__author__ = 'Nathan Meadows'

from cgi import escape
from py.environment import *


class Admin(Urls):

    @staticmethod
    def index(environ, start_response):
        from py.environment import Env

        tables = Env.db.gettables()
        content = '<br />'.join(tables)

        return Urls.wrapTemplate(content)

