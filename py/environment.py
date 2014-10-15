__author__ = 'Nathan Meadows'

import logging

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


class Env(object):

    db = None
    if Config.dbtype == 'postgresql':
        from py.postgresql import Postgres
        db = Postgres()
    elif Config.dbtype == 'sqlite3':
        from py.sqlite import Sqlite
        db = Sqlite()



<<<<<<< HEAD
=======

>>>>>>> origin/master
    @staticmethod
    def log(message, level='warn'):

        loglevel = {
            'debug': 10,
            'info': 20,
            'warn': 30,
            'error': 40,
            'critical': 50,
                    }.get(Config.loglevel, 30)
        logging.basicConfig(filename=Config.loglocation,
                            level=loglevel,
                            format='%(asctime)s %(levelname)s %(message)s')

        if level == 'debug':
            logging.debug(message)
        elif level == 'info':
            logging.info(message)
        elif level == 'warn':
            logging.warning(message)
        elif level == 'error':
            logging.error(message)
        else:
            logging.critical(message)

    def __init__(self):
        pass

