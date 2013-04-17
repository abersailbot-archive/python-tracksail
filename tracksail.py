# Python wrapper to interface with Tracksail-AI

# Copyright 2013 Louis Taylor

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import socket

def _float(v):
    if v:
        return float(v[:-1])
    else:
        return None

class Tracksail(object):
    class _Waypoint(object):
        """The target point"""
        def __init__(self, tracksail):
            self.tracksail = tracksail

        def __str__(self):
            return 'distance: {}m, waypoint #{}, direction: {}'.format(
                                                                self.distance,
                                                                self.number,
                                                                self.direction
                                                                      )
        
        @property
        def direction(self):
            return self.tracksail._send_command('get waypointdir')

        @property
        def number(self):
            return self.tracksail._send_command('get waypointnum')

        @property
        def distance(self):
            return self.tracksail._send_command('get waypointdist')

        def next(self):
            self.tracksail._send_command('set waypoint')

    def __init__(self):
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._rudderPos = 0
        self._waypoint = self._Waypoint(self)

    def connect(self, host='localhost', port=5555):
        """Connect to tracksail"""
        self._socket.connect((host, port))

    def _send_command(self, command):
        self._socket.send(command)
        return self._socket.recv(256)

    def close(self):
        """Close the connection to tracksail"""
        print 'closing connection to tracksail...'
        self._socket.close()

    def windDirection(self):
        """Return the direction of the wind"""
        return _float(self._send_command('get wind_dir'))

    def bearing(self):
        """Return the bearing of the boat"""
        return _float(self._send_command('get compass'))

    @property
    def sailPosition(self):
        return _float(self._send_command('get sail'))

    @sailPosition.setter
    def sailPosition(self, value):
        self._send_command('set sail {}'.format(int(value)))

    @property
    def rudderPosition(self):
        return self._rudderPos

    @rudderPosition.setter
    def rudderPosition(self, value):
        self._send_command('set rudder {}'.format(int(value)))

    @property
    def waypoint(self):
        return self._waypoint

    @property
    def latitude(self):
        return self._send_command('get northing')

    @property
    def longitude(self):
        return self._send_command('get easting')


if __name__ == '__main__':
    t = Tracksail()
    t.connect()
    print t.windDirection
    print t.sailPosition
    t.sailPosition = 320
    print t.sailPosition
    print t.waypoint
    t.waypoint.next()
    print t.waypoint
    print t.waypoint.direction
    t.close()
