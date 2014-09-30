import sys
sys.path.append('../')
sys.path.append('negativenull.com/')
from py.functions import Functions



def application(environ, start_response):
    cont = (open('negativenull.com/header.html').read())
    cont += Functions.test('from functions.py')
    cont += (open('negativenull.com/footer.html').read())

    start_response('200 OK', [('Content-Type', 'text/html')])
    return [cont]