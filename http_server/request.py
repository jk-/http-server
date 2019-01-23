
from http_server.headers import HttpHeaders

# could use inheritance for list object
# should be tuples and this is in an ugly spot
class Request(object):

    def __init__(self, context):
        self.headers = HttpHeaders(context)
        self.get_params = ""
        self.request_path = ""

        self.status = self.headers.get_status()
        self.request_path = self._set_request_path()
        self.get_params = self._set_get_params()

    def _set_request_path(self):
        return self.status.split(" ")[1]

    def _set_get_params(self):
        if "?" in self.request_path:
            return self.request_path.split("?")[1]
