import socket

from app import SimpleApp
from app.router import Router

from http_server import Server

app = SimpleApp()

@Router.route("/")
def index():
    return "This is the index page"

@Router.route("/test")
def test():
    return "<strong>This is the test page<strong>"

@Router.route("/sayhello", methods=["GET"])
def hello_no_name():
    return "Hello"

@Router.route("/sayhello/<username>", methods=["GET"])
def hello(username):
    return "Hello {0}".format(username)

if __name__ == "__main__":
    http_server = Server('', 1337, 5)
    http_server.run(app)

    try:
        while True:
            try:
                http_server.handle_request()
            finally:
                http_server.stop()
    except KeyboardInterrupt:
        print("Goodbye\n")
