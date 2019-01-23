import socket

from app import SimpleApp
from http_server import Server

app = SimpleApp()

@app.route("/")
def index():
    return "This is the index page"

@app.route("/test")
def test():
    return "<doctype html><html><header><title>Test</title></header><body><strong>This is the test page<strong></body></html>"

@app.route("/sayhello/<username>", methods=["GET"])
def hello(username):
    return "Hello {0}".format(username)

if __name__ == "__main__":
    http_server = Server('', 1337, 5)
    http_server.run(app)
    while 1:
        try:
            http_server.handle_request()
        finally:
            http_server.stop()
