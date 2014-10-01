import sys
sys.path.append('../')
sys.path.append('negativenull.com/')
from py.functions import Functions
from py.tag import Tag


def application(environ, start_response):
    cont = (open('negativenull.com/header.html').read())
    tags = Tag('tag')


    start_response('200 OK', [('Content-Type', 'text/html')])
    return [tags.processTags(cont)]