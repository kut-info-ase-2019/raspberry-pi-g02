#!/usr/bin/python

###########################################################################
#Filename      :pythontest.py
#Description   :blink LED
#Author        :alan
#Website       :www.osoyoo.com
#Update        :2017/06/20
############################################################################

import RPi.GPIO as GPIO
import time

# set GPIO 0 as LED pin
RPIN = 22
YPIN = 17
GPIN = 4

#print message at the begining ---custom function
def print_message():
    print ('|********************************|')
    print ('|            blink LED           |')
    print ('|      ------------------------- |')
    print ('|        LED connect to GPIO0    |')
    print ('|                                |')
    print ('|        LED will blink at 500ms |')
    print ('|      ------------------------- |')
    print ('|                                |')
    print ('|                          OSOYOO|')
    print ('|********************************|\n')
    print ('Program is running...')
    print ('Please press Ctrl+C to end the program...')

#setup function for some setup---custom function
def setup():
    GPIO.setwarnings(False)
    #set the gpio modes to BCM numbering
    GPIO.setmode(GPIO.BCM)
    #set RPIN's mode to output,and initial level to LOW(0V)
    GPIO.setup(RPIN,GPIO.OUT,initial=GPIO.LOW)
    GPIO.setup(YPIN,GPIO.OUT,initial=GPIO.LOW)
    GPIO.setup(GPIN,GPIO.OUT,initial=GPIO.LOW)
    

#main function
def main():
    #print info
    print_message()
    while True:
       GPIO.output(RPIN,GPIO.HIGH)
       print('...RLED ON\n')
       time.sleep(0.5)

       GPIO.output(RPIN,GPIO.LOW)
       print('RLED OFF...\n')
       time.sleep(0.5)

       GPIO.output(YPIN,GPIO.HIGH)
       print('...YLED ON\n')
       time.sleep(0.5)
       
       GPIO.output(YPIN,GPIO.LOW)
       print('YLED OFF...\n')
       time.sleep(0.5)

       GPIO.output(GPIN,GPIO.HIGH)
       print('...GLED ON\n')
       time.sleep(0.5)
       
       GPIO.output(GPIN,GPIO.LOW)
       print('GLED OFF...\n')
       time.sleep(0.5)
       pass
    pass

#define a destroy function for clean up everything after the script finished
def destroy():
    #turn off LED
    GPIO.output(RPIN,GPIO.LOW)
    #release resource
    GPIO.cleanup()
#
# if run this script directly ,do:
if __name__ == '__main__':
    setup()
    try:
            main()
    #when 'Ctrl+C' is pressed,child program destroy() will be executed.
    except KeyboardInterrupt:
        destroy()

   

