__author__ = 'Nathan Meadows'
import psycopg2
import psycopg2.extras
from py.environment import *


class Postgres(DB):

    def __init__(self):
        DB.__init__(self)
        self.conn = psycopg2.connect("dbname=%s user=%s password=%s port=%d" % (Config.dbname,
                                                                                Config.dbusername,
                                                                                Config.dbpassword,
                                                                                Config.dbport)
                                     )

    def query(self, query, returnall=False, returnone=False):
        self.cur = self.conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        self.cur.execute(query)
        if returnall:
            return self.cur.fetchall()
        elif returnone:
            return self.cur.fetchone()
