import re

# just assume the route matches a string for now
_reg_ex = re.compile(r'''
    (?P<static>[^<]*)
    <
    (?P<variable>[a-zA-Z_][a-zA-Z0-9_]*)
    >
    ''', re.VERBOSE)

def parse_rule(rule):
    pos = 0
    end = len(rule)
    do_match = _reg_ex.match
    used_names = set()
    while pos < end:
        m = do_match(rule, pos)
        if m is None:
            break
        data = m.groupdict()
        if data['static']:
            yield None, None, data['static']
        variable = data['variable']
        used_names.add(variable)
        # apartt of static generator above
        yield 'str', None, variable
        pos = m.end()
    if pos < end:
        remaining = rule[pos:]
        if '>' in remaining or '<' in remaining:
            raise ValueError('malformed url rule: %r' % rule)
        yield None, None, remaining

class Router:
    map = []
    view_func = {}

    def __init__(self):
        pass

    # decorator for injecting routes into the app
    def route(self, path_route, **options):
        def route_decorator(f):
            endpoint = options.pop('endpoint', None)
            self.compile(path_route, endpoint, f, **options)
            return f
        return route_decorator

    def compile(self, path_route, endpoint=None, view_func=None, **options):
        if endpoint is None:
            endpoint = view_func.__name__
        self.view_func[endpoint] = view_func
        itr = 0
        for converter, args, variable in parse_rule(path_route):
            if converter is None:
                self.map[itr] = { path_route : endpoint }
            else:
                # would have to decriment the itr to push into previous parse
                pass
            itr += 1
        print(self.map)

    '''
    Need to loop over parse_rule and split out converter, args, variable
    if converter the variable is attached to the previous generater
    /sayhello/<username>
    if static identified from parse_url split on / to get path
    add to url routes and atttached the dispatcher
    would need to keep track of index on the itr to attache variable
    need to convert the variable to a string|int
    '''
