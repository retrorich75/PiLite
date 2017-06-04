#!/usr/bin/env python
#--------------------------------------
#
# Pi-Lite Hello World Example
# (with repeating message)
#
# Author : Matt Hawkins
# Date   : 01/10/2013
#
# http://www.raspberrypi-spy.co.uk/
#
#--------------------------------------

import sys
import serial
import time

# Define message complete with
# carriage return at the end
message1 = "Hello World!\r"
message2 = "Pi-Lite messages are easy!\r"

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
    
while True:    
    
  # Send message 1 to the Pi-Lite
  print message1
  s.write(message1)  

  # Short delay to allow the
  # 12 character message to finish
  time.sleep(6)

  # Send message 2 to the Pi-Lite
  print message2
  s.write(message2)  

  # Short delay to allow the
  # 26 character message to finish
  time.sleep(12)