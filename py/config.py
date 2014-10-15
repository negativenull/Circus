__author__ = 'Nathan Meadows'


class Config:

    siteroot = '/var/www/Circus/'

    dbtype = 'postgresql'

    #for postgresql
    dbname = 'negativenullcom'
    dbhost = 'localhost'
    dbport = 5432
    dbusername = 'nathan'
    dbpassword = ''

    #for sqlite3
    dblocation = '/Users/nathan/test.db'

    siteTitle = 'Circus Framework'

    #logging
    loglocation = '/users/nathan/circus.log'
    loglevel = 'warn'  # debug, info, warn, error, critical

    def __init__(self):
        pass
