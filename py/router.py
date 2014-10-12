from py.environment import *

#map urls to function
router = [
            (r'^$', Urls.index),
            (r'hello/?$', Hello.hello),
            (r'hello/(.+)$', Hello.hello),
            (r'page/?$', Page.page),
            (r'page/(.+)$', Page.page)
        ]