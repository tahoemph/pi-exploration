#!/usr/bin/env python
 
# This bit of code sets up a temperature sensor and reads
# values.

import RPi.GPIO as GPIO 
import time
 
 
GPIO.setmode(GPIO.BCM)

SENSORS = [4]
for sensor in SENSORS:
	GPIO.setup(sensor, GPIO.IN)
 
while True:
	for sensor in SENSORS:
		print GLIO.input(sensor)
	time.sleep(0.5)
