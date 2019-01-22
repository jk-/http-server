
from http_server.headers import HttpHeaders

# could use inheritance for list object
# should be tuples and this is in an ugly spot
class Response(object):

    def __init__(self):
        self.headers = HttpHeaders()
        self.body = ""

    def addHeader(self, key, value):
        self.headers.add(key, value)

    def addStatus(self, value):
        self.status = value

    def addBody(self, value):
        self.headers.add('Content-Length', len(value))
        self.body = value

    def packed(self, byte=False):
        pack = self.status + "\r\n" + self.headers.concat() + "\r\n\r\n" + self.body
        return bytes(pack, 'utf-8') if byte else pack
