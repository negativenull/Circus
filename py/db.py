__author__ = 'Nathan Meadows'

from py.environment import *


class DB:

    conn = None
    cur = None

    def __init__(self):
        pass

    def fetchall(self):
        return self.cur.fetchall()

    def fetchone(self):
        return self.cur.fetchone()

    def numrows(self):
        return self.cur.rowcount()
