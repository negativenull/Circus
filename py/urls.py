__author__ = 'Nathan Meadows'

from py.tag import Tag
from py.db import DB


class Urls:

    tag = Tag('tag')

    def __init__(self):
        pass

    @staticmethod
    def wrapTemplate(content):
        sitetags = Tag('site')
        header = open('negativenull.com/views/header.html').read()
        header = sitetags.processTags(header)

        footer = open('negativenull.com/views/footer.html').read()
        footer = sitetags.processTags(footer)

        return header+content+footer

    @staticmethod
    def index(environ, start_response):
        cont = (open('negativenull.com/views/index.html').read())
        pagetags = Tag('tag')
        return [Urls.wrapTemplate(pagetags.processTags(cont))]





    @staticmethod
    def not_found(environ, start_response):
        cont = (open('negativenull.com/views/404.html').read())
        return [Urls.wrapTemplate(cont)]

