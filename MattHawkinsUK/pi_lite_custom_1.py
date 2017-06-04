#!/usr/bin/env python
#--------------------------------------
#
# Pi-Lite Custom Example #1
#
# Author : Matt Hawkins
# Date   : 06/10/2013
#
# http://www.raspberrypi-spy.co.uk/
#
#--------------------------------------

import sys
import serial
import time

# Define two sprites
sprite1 = '000000000000000000000011110000100010111001001100100101010010101010010101100100101111001001000100010000011110000000000000000000'
sprite2 = '000000000000000000000000000000011111011111111111111111110011111110011111111111111011111111000011111000000000000000000000000000'

# Configure Pi serial port
s = serial.Serial()
s.baudrate = 9600
s.timeout = 0
s.port = "/dev/serial0"

try:
    # Open serial port
    s.open()
except serial.SerialException, e:
    # There was an error
    sys.stderr.write("could not open port %r: %s\n" % (port, e))
    sys.exit(1)

print "Serial port ready"

# Clear display
s.write("$$$ALL,OFF\r")

# Send Sprite 1 to the Pi-Lite
print "Sprite 1"
s.write('$$$F' + sprite1 + '\r')

# Short delay
time.sleep(2)

# Send Sprite 2 to the Pi-Lite
print "Sprite 2"
s.write('$$$F' + sprite2 + '\r')

# Short delay
time.sleep(2)

# Quit
print "Good bye"