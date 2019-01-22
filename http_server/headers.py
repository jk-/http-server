
class HttpHeaders(object):

    params = {}

    def __init__(self, context=None):
        self.context = context
        if context:
            self._parse_context()

    def _parse_context(self):
        s = self.context.decode('utf-8').split("\r\n")
        self.status = s[0]
        for i in s[1:-2]:
            if i is None:
                continue
            (key, value) = i.split(": ")
            self.params[key] = value

    def add(self, key, value):
        self.params[key] = value

    def getRequestPath(self):
        return self.status.split(' ')[1]

    def concat(self):
        t = []
        for i in self.params:
            t.append(str(i) + ": " + str(self.params[i]))
        return "\r\n".join(t)

    def __str__(self):
        return "===".join(self.params)
