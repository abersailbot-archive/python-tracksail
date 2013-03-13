import socket

class Tracksail(object):
    def __init__(self):
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self, host='localhost', port=5555):
        self._socket.connect((host, port))

    def _send_command(self, command):
        self._socket.send(command)
        return self._socket.recv(256)

    def close(self):
        self._socket.close()

if __name__ == '__main__':
    t = Tracksail()
    t.connect()
    print t._send_command('get wind_dir')
    t.close()
