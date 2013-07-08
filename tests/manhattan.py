#!/usr/bin/env python
##
# Barbot v0.1: Little Brobot Serial Controller for Manhattan
##
from pydrinks import *

__SERIAL_PORT__ = '/dev/tty.usbserial-A9007KVJ'

manhattan = Drink('manhattan', [('whiskey',2), ('vermouth',1)])
a = BarBot(__SERIAL_PORT__, [Dispenser('whiskey', 'a', 'A'), Dispenser('vermouth', 'b', 'B')], [manhattan])
a.make_drink('manhattan', 10)
