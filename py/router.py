from py.urls import Urls
router = [
            (r'^$', Urls.index),
            (r'hello/?$', Urls.hello),
            (r'hello/(.+)$', Urls.hello)
        ]