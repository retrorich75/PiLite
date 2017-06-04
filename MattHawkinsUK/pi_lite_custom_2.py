#!/usr/bin/env python
#--------------------------------------
#
# Pi-Lite Custom Example #2
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

# Define padlock list containing two sprites
padlock = ['000000000000000000000000000000011111011111111111111111110011111110011111111111111011111111000011111000000000000000000000000000',
           '011100000111100000110000000110011111111111111011111111000011111000011111000011111000011111000011111000000000000000000000000000']

# Define list to describe each sprite
description = ['Locked','Unlocked']

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

# Initialise some variables
loop  = True
frame = 0

while loop:

    s.write('$$$F' + padlock[frame] + '\r')
    print description[frame]

    inp = raw_input("Press [Enter] to toggle padlock. [x-Enter] to quit.")

    if inp.lower()!="x":
      # Toggle frame to display
      frame = 1 - frame
    else:
      # Exit loop
      loop = False

# Quit
print "Good bye"