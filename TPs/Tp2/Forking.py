
import socket
from socketserver import ForkingMixIn
from http.server import BaseHTTPRequestHandler, HTTPServer

class ForkingHTTPServer(ForkingMixIn, HTTPServer):
    def __init__(self, server_address, RequestHandlerClass):
        if ':' in server_address[0]:                
            self.address_family = socket.AF_INET6
        else:
            self.address_family = socket.AF_INET
        super().__init__(server_address, RequestHandlerClass)