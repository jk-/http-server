
from .router import Router

class SimpleApp():

    def __init__(self):
        self.router = Router()

    def dispatch_request(self, path_route):
        return self.router.get_route_dispatch(path_route)
