from py.urls import Urls

#map urls to function
router = [
            (r'^$', Urls.index),
            (r'hello/?$', Urls.hello),
            (r'hello/(.+)$', Urls.hello),
            (r'pages/(.+)$', Urls.pages)
        ]