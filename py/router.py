from py.environment import *
from controllers.page import Page
from controllers.hello import Hello
from controllers.admin import Admin

#map urls to function
router = [
            (r'^$', Urls.index),
            (r'hello/?$', Hello.hello),
            (r'hello/(.+)$', Hello.hello),
            (r'page/?$', Page.page),
            (r'page/(.+)$', Page.page),
            (r'^$', Admin.index),
        ]
