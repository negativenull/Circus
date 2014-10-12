__author__ = 'Nathan Meadows'


class Config:

    siteroot = '/home/nathan/PycharmProjects/Circus/'

    dbtype = 'sqlite3'

    #for postgresql
    dbname = 'negativenullcom'
    dbhost = 'localhost'
    dbport = 5432
    dbusername = 'nathan'
    dbpassword = ''

    #for sqlite3
    dblocation = '/home/nathan/test.db'

    siteTitle = 'Circus Framework'

    #logging
    loglocation = '/home/nathan/circus.log'
    loglevel = 'debug'  # debug, warn, error

    def __init__(self):
        pass
