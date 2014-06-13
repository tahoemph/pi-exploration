#!/usr/bin/env python

import RPi.GPIO as GPIO, time, os

SLEEP_TIME = 1

GPIO.setmode(GPIO.BCM)
GREEN_LED = 24
RED_LED = 23
BLUE_LED = 18

GPIO.setup(GREEN_LED, GPIO.OUT)
GPIO.setup(RED_LED, GPIO.OUT)
GPIO.setup(BLUE_LED, GPIO.OUT)

try:

    while True:
        print "Red Light"
        GPIO.output(GREEN_LED, False)
        GPIO.output(RED_LED, True)
        GPIO.output(BLUE_LED, False)
        time.sleep(SLEEP_TIME)  
        
        print "Blue Light"
        GPIO.output(RED_LED, False)
        GPIO.output(BLUE_LED, True)
        GPIO.output(GREEN_LED, False)
        time.sleep(SLEEP_TIME)          
        
        print "Green Light"
        GPIO.output(BLUE_LED, False)
        GPIO.output(GREEN_LED, True)
        GPIO.output(RED_LED, False)
        time.sleep(SLEEP_TIME)
        
except KeyboardInterrupt:
      GPIO.cleanup()
