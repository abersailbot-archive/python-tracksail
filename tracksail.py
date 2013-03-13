import socket

def _float(v):
    print 'coverting "%s"' % v
    if v:
        return float(v[:-1])
    else:
        return None

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

    @property
    def windDirection(self):
        return _float(self._send_command('get wind_dir'))

    @property
    def compass(self):
        return _float(self._send_command('get compass'))

    @property
    def sail(self):
        return _float(self._send_command('get sail'))

    @sail.setter
    def sail(self, value):
        print 'set sail {}'.format(int(value))
        self._send_command('set sail {}'.format(int(value)))


if __name__ == '__main__':
    t = Tracksail()
    t.connect()
    print t.windDirection
    print t.sail
    t.sail = 10
    print t.sail
    t.close()
