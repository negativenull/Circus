def application(environ, start_response):
    cont = (open('negativenull.com/index.html').read())
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [cont]