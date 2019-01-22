

# this needs to abstract a server environment for handling requests
class SimpleApp():

    url_map = {}
    view_func = {}

    def __init__(self):
        pass

    def add_url_rule(self, path_route, endpoint=None, view_func=None, **options):
        if endpoint is None:
            endpoint = view_func.__name__
        self.url_map[path_route] = endpoint
        self.view_func[endpoint] = view_func

    def route(self, path_route, **options):
        def route_decorator(f):
            endpoint = options.pop('endpoint', None)
            self.add_url_rule(path_route, endpoint, f, **options)
            return f
        return route_decorator

    # dont like this, not decoupled
    def dispatchRequest(self, path_route):
        if path_route in self.url_map.keys():
            return self.view_func[self.url_map[path_route]]()
        else:
            return ""
