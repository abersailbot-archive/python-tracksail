import socket

def _float(v):
    print 'coverting "%s"' % v
    if v:
        return float(v[:-1])
    else:
        return None

class Tracksail(object):
    class _Waypoint(object):
        def __init__(self, tracksail):
            self.tracksail = tracksail
        
        @property
        def direction(self):
            return self.tracksail._send_command('get waypointdir')

        @property
        def number(self):
            return self.tracksail._send_command('get waypointnum')

        @property
        def distance(self):
            return self.tracksail._send_command('get waypointdist')

    def __init__(self):
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._rudderPos = 0
        self._waypoint = self._Waypoint(self)

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
    def sailPosition(self):
        return _float(self._send_command('get sail'))

    @sailPosition.setter
    def sailPosition(self, value):
        print 'set sail {}'.format(int(value))
        self._send_command('set sail {}'.format(int(value)))

    @property
    def rudderPosition(self):
        return self._rudderPos

    @rudderPosition.setter
    def sailPosition(self, value):
        print 'set rudder {}'.format(int(value))
        self._send_command('set rudder {}'.format(int(value)))

    def next_waypoint(self):
        self._send_command('set waypoint')

    @property
    def waypoint(self):
        return self._waypoint

if __name__ == '__main__':
    t = Tracksail()
    t.connect()
    print t.windDirection
    print t.sailPosition
    t.sailPosition = 320
    print t.sailPosition
    print t.waypoint
    print t.waypoint.direction
    t.close()
