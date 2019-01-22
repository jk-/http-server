
from http_server.headers import HttpHeaders

# could use inheritance for list object
# should be tuples and this is in an ugly spot
class Request(object):

    def __init__(self, context):
        self.headers = HttpHeaders(context)

    def getRequestPath(self):
        return self.headers.getRequestPath()
