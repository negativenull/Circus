__author__ = 'Nathan Meadows'

from py.environment import *
import sqlite3


class Sqlite(DB):

    def __init__(self):
        DB.__init__(self)
        self.conn = sqlite3.connect(Config.dblocation)
        self.conn.row_factory = sqlite3.Row

    def query(self, query, returnall=False, returnone=False):
        self.cur = self.conn.cursor()
        self.cur.execute(query)
        if returnall:
            return self.cur.fetchall()
        elif returnone:
            return self.cur.fetchone()

    def gettables(self):
        query = """SELECT name FROM my_db.sqlite_master WHERE type='table';"""
        return self.query(query, returnall=True)