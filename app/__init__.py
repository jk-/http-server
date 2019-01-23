
from .router import Router

class SimpleApp():

    def __init__(self):
        self.router = Router()

    def dispatch_request(self, path_route):
        # need to loop through router map
        '''
            if path_route in self.router.map.keys():
                return self.view_func[self.url_map[path_route]]

        '''
        pass
