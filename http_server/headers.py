
class HttpHeaders(object):

    params = {}

    def __init__(self, context=None):
        self.context = context
        if context:
            self._parse_context()

    def _parse_context(self):
        self.context_parsed = self.context.decode('utf-8').split("\r\n")
        for i in self.context_parsed[1:-2]:
            if i is None:
                continue
            (key, value) = i.split(": ")
            self.add(key, value)

    def get_status(self):
        return self.context_parsed[0] if self.context_parsed else ""

    def add(self, key, value):
        self.params[key] = value

    def concat(self):
        t = []
        for i in self.params:
            t.append(str(i) + ": " + str(self.params[i]))
        return "\r\n".join(t)

    def __str__(self):
        return "===".join(self.params)
