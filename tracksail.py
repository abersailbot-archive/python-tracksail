import socket

class Tracksail(object):
    def __init__(self):
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(host='localhost', port=5555):
        self._socket.connect(host, port)
