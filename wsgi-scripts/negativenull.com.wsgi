def application(environ, start_response):
    cont = (open('negativenull.com/header.html').read())

    cont += "hello world"

    cont += (open('negativenull.com/footer.html').read())

    start_response('200 OK', [('Content-Type', 'text/html')])
    return [cont]