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

if __name__ == "__main__":
    # not ideal just testing a request and response
    http_server = Server('', 1337, 5)
    http_server.env(app)
    http_server.run()
    while 1:
        http_server.accept()
