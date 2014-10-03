__author__ = 'Nathan Meadows'
import psycopg2
import psycopg2.extras

from config.config import Config


class DB:

    conn = None
    cur = None

    def __init__(self):
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

    def fetchall(self):
        return self.cur.fetchall()

    def fetchone(self):
        return self.cur.fetchone()

    def numrows(self):
        return self.cur.rowcount()

'''
# Connect to an existing database
>>> conn = psycopg2.connect("dbname=test user=postgres")

# Open a cursor to perform database operations
>>> cur = conn.cursor()

# Execute a command: this creates a new table
>>> cur.execute("CREATE TABLE test (id serial PRIMARY KEY, num integer, data varchar);")

# Pass data to fill a query placeholders and let Psycopg perform
# the correct conversion (no more SQL injections!)
>>> cur.execute("INSERT INTO test (num, data) VALUES (%s, %s)",
...      (100, "abc'def"))

# Query the database and obtain data as Python objects
>>> cur.execute("SELECT * FROM test;")
>>> cur.fetchone()
(1, 100, "abc'def")

# Make the changes to the database persistent
>>> conn.commit()

# Close communication with the database
>>> cur.close()
>>> conn.close()
'''