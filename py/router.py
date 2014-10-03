from py.urls import Urls
from controllers.page import Page

#map urls to function
router = [
            (r'^$', Urls.index),
            (r'hello/?$', Urls.hello),
            (r'hello/(.+)$', Urls.hello),
            (r'page/?$', Page.page),
            (r'page/(.+)$', Page.page)
        ]