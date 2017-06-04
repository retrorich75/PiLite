#!/usr/bin/env python
#--------------------------------------
#
# Pi-Lite Dice Thrower Example
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
import random

# Define list which contain dice graphic frames
dice = ['000000000000000000000000000000000000000000000000000000000110000000110000000000000000000000000000000000000000000000000000000000',
        '000000000000000000110000000110000000000000000000000000000000000000000000000000000000000000000000110000000110000000000000000000',
        '000000000000000000110000000110000000000000000000000000000110000000110000000000000000000000000000110000000110000000000000000000',        
        '000000000000000000110000110110000110000000000000000000000000000000000000000000000000000000110000110110000110000000000000000000',
        '000000000000000000110000110110000110000000000000000000000110000000110000000000000000000000110000110110000110000000000000000000',
        '000000000000000000000000000000000000110110110110110110000000000000000000110110110110110110000000000000000000000000000000000000']

def showDice(number):
  # Function to display specified dice number
  command = "$$$F" + dice[number-1] + "\r"
  s.write(command)
  time.sleep(0.5)
   
# Configure Pi serial port
s = serial.Serial()
s.baudrate = 9600
s.timeout = 0
s.port = "/dev/serial0"
  
random.seed()
  
try:
    # Open serial port
    s.open()
except serial.SerialException, e:
    sys.stderr.write("could not open port %r: %s\n" % (port, e))
    sys.exit(1)

# Turn off all LEDs
s.write("$$$ALL,OFF\r")
time.sleep(0.5)

loop = True

while loop:

    inp = raw_input("Press [Enter] to throw the dice:")

    if inp.lower()!="x":
      number = random.randint(1,6)
      showDice(number)
      print("You rolled a " + str(number))
      time.sleep(2)
    else:
      loop = False

# Turn off all LEDs    
s.write("$$$ALL,OFF\r")

print("Goodbye!")
