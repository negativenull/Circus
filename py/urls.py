__author__ = 'Nathan Meadows'

from py.environment import *


class Urls:

    tag = Tag('tag')

    def __init__(self):
        pass

    @staticmethod
    def wrapTemplate(content):
        sitetags = Tag('site')
        header = open(Config.siteroot+'views/header.html').read()
        header = sitetags.processTags(header)

        footer = open(Config.siteroot+'views/footer.html').read()
        footer = sitetags.processTags(footer)

        return header+content+footer

    @staticmethod
    def index(environ, start_response):
        cont = (open(Config.siteroot+'views/index.html').read())
        pagetags = Tag('tag')
        return [Urls.wrapTemplate(pagetags.processTags(cont))]





    @staticmethod
    def not_found(environ, start_response):
        cont = (open(Config.siteroot+'views/404.html').read())
        return [Urls.wrapTemplate(cont)]

