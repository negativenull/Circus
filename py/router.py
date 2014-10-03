from py.urls import Urls
from controllers.page import Page
from controllers.hello import Hello

#map urls to function
router = [
            (r'^$', Urls.index),
            (r'hello/?$', Hello.hello),
            (r'hello/(.+)$', Hello.hello),
            (r'page/?$', Page.page),
            (r'page/(.+)$', Page.page)
        ]