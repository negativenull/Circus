from py.urls import Urls

#map urls to function
router = [
            (r'^$', Urls.index),
            (r'hello/?$', Urls.hello),
            (r'hello/(.+)$', Urls.hello),
            (r'page/?$', Urls.page),
            (r'page/(.+)$', Urls.page)
        ]