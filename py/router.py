urls = [
            (r'^$', Urls.index),
            (r'hello/?$', Urls.hello),
            (r'hello/(.+)$', Urls.hello)
        ]