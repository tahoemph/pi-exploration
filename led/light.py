#!/usr/bin/env python
 
import RPi.GPIO as GPIO 
 
 
GPIO.setmode(GPIO.BCM)
GREEN_LED = 18
RED_LED = 25
GPIO.setup(GREEN_LED, GPIO.OUT)
GPIO.setup(RED_LED, GPIO.OUT)
 
GPIO.output(GREEN_LED, True)
GPIO.output(RED_LED, GPIO.HIGH)
while True:
    pass
