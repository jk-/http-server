import socket
import sys
import inspect

from http_server.request import Request
from http_server.response import Response

class Server(object):

    running = False

    def __init__(self, host="", port=1337, queue_size=0):
        self.host = host
        self.port = port
        self.queue_size = 5
        self.client = ""

    def run(self, env):
        if not self.running:
            # catch errors
            self.running = True
            self.env = env
            self._create_socket()
            self._bind()
            self._listen()

    def stop(self):
        if self.client:
            self.client.shutdown(socket.SHUT_RDWR)
            self.client.close()

    def _create_socket(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._set_socket_options()

    def _set_socket_options(self):
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    def _bind(self):
        self.s.bind((self.host, self.port))

    def _listen(self):
        self.s.listen(self.queue_size)

    def read_data(self):
        (self.client, self.addr) = self.s.accept()
        self.client_data = self.client.recv(1024) # context
        self.request = Request(self.client_data)

    def handle_request(self):
        self.read_data()

        response = Response()
        response.add_header('Content-type', 'text/html')

        try:
            response.add_status('HTTP/1.1 200 OK')
            f = self.env.dispatch_request(self.request.request_path)
            response.add_body(f())
        except:
            response.add_status('HTTP/1.1 404 Not Found')
            response.add_body("error")

        self.client.sendall(response.packed(byte=True))
