from http_server.headers import HttpHeaders

class Response(object):

    def __init__(self):
        self.headers = HttpHeaders()
        self.body = ""

    def add_header(self, key, value):
        self.headers.add(key, value)

    def add_status(self, value):
        self.status = value

    def add_body(self, value):
        self.headers.add('Content-Length', len(value))
        self.body = value

    def packed(self, byte=False):
        pack = self.status + "\r\n" + self.headers.concat() + "\r\n\r\n" + self.body
        return bytes(pack, 'utf-8') if byte else pack
