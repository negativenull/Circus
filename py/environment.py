__author__ = 'Nathan Meadows'


from py.config import Config
from py.tag import Tag
from py.urls import Urls
from py.db import DB
from py.functions import Functions


#controllers go here
from controllers.page import Page
from controllers.hello import Hello


#router must be last
from py.router import router


if Config.dbtype == 'postgresql':
    from py.postgresql import Postgres
    db = Postgres()
elif Config.dbtype == 'sqlite3':
    from py.sqlite import Sqlite
    db = Sqlite()

