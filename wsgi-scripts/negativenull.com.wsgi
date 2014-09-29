def application(environ, start_response):
    cont = (open('index.html').read())
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [cont]