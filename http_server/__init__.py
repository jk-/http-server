import socket

from http_server.request import Request
from http_server.response import Response

class Server(object):

    #__slots__ = ["host", "port", "queue_size", "client", "addr", "headers"]

    running = False

    def __init__(self, host="", port=1337, queue_size=0):
        self.host = host
        self.port = port
        self.queue_size = 5

    def env(self, env):
        self.env = env

    def run(self):
        if not self.running:
            # catch errors
            self.running = True
            self._create_socket()
            self._bind()
            self._listen()

    def stop(self):
        if self.running:
            # catch errors
            self.client.shutdown(socket.SHUT_RDWR)
            self.client.close()
            self.running = False

    def _create_socket(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._set_socket_options()

    def _set_socket_options(self):
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    def _bind(self):
        self.s.bind((self.host, self.port))

    def _listen(self):
        self.s.listen(self.queue_size)

    def accept(self):
        (self.client, self.addr) = self.s.accept()
        self.client_data = self.client.recv(1024) # context
        if self.client_data:
            self.request = Request(self.client_data)
            self.handle_request()

    # would have to build request object and send request object
    def handle_request(self):
        response = Response()
        response.addStatus('HTTP/1.1 200 OK')
        response.addHeader('Content-type', 'text/html')
        response.addBody(self.env.dispatchRequest(self.request.getRequestPath()))
        self.client.sendall(response.packed(byte=True))
        self.stop()
