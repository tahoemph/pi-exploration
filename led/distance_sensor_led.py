#!/usr/bin/env python
 
# This bit of code sets up the distance sensor and a bar graph
# (series of leds) to show a scaled value.

import RPi.GPIO as GPIO 
import time
 
 
GPIO.setmode(GPIO.BCM)
TRIG_PIN = 23
ECHO_PIN = 24
GPIO.setup(TRIG_PIN, GPIO.OUT)
GPIO.setup(ECHO_PIN, GPIO.IN)

LEDS = [25, 18, 4]
for led in LEDS:
	GPIO.setup(led, GPIO.OUT)
 
time.sleep(0.5)

while True:
	GPIO.output(TRIG_PIN, True)
	time.sleep(0.00001)
	GPIO.output(TRIG_PIN, False)
	while GPIO.input(ECHO_PIN) == 0:
	    pass
	start = time.time()
	while GPIO.input(ECHO_PIN) == 1:
	    pass
	stop = time.time()
	elapsed = stop - start
	distance = elapsed * 35000.0 / 2.0
	scaled = distance / (35.0/len(LEDS))
	print scaled
	for led in range(len(LEDS)):
		GPIO.output(LEDS[led], False)
	for led in range(min(int(scaled), len(LEDS))):
		GPIO.output(LEDS[led], True)
	time.sleep(0.5)
