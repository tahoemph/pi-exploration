#!/usr/bin/env python

import logging
import RPIO, time, os
from RPIO import PWM
import requests
import sys
import threading
import time

logging.basicConfig(level=logging.WARN)
PWM.set_loglevel(PWM.LOG_LEVEL_ERRORS)
RPIO.setmode(RPIO.BCM)
servo = None

def decode_color(color):
    if color.endswith('anime'):
	return 0
    elif color == 'blue':
        return 1
    else:
        return -1

def get_config():
	return { 'examplesvc' : {
		'button' : 17,
		'led' : 0,#4,
		'status_url': "http://maria.saymedia.com/job/examplesvc/job/master/api/json?tree=color",
		'action_url': "http://maria.saymedia.com/job/examplesvc/job/test-ci/build?delay=0sec"
		}
	}

def key_hit(gpio_id, val):
	print "force build!"
	requests.get("http://maria.saymedia.com/job/examplesvc/job/test-ci/build?delay=0sec")
	print "done"

def init_button_led(config):
	config['comms'] = 0
	if config['button']:
		RPIO.setup(config['button'], RPIO.IN)
		RPIO.add_interrupt_callback(config['button'], key_hit,
			threaded_callback=True, debounce_timeout_ms=100)
		RPIO.wait_for_interrupts(threaded=True)
	if config['led']:
		t = threading.Thread(target=blink_lights, args=(config,))
		t.daemon = True
		t.start()

def blink_lights(config):
    	width = 100
	if not servo:
		servo = PWM.Servo()
    	while True:
		ans = config['comms']
		if ans == 1:
			width = 2000
		elif ans == -1:
			width = 0
		else:
			width = (width + 100) % 2000
		servo.set_servo(config['led'], width)
		time.sleep(1.0/20)

def main():
	config = get_config()
	try:
		for service, service_config in config.iteritems():
			init_button_led(service_config)
		# There is actually an endpoint to get the status of the
		# world which should be used here.
		while True:
			for service, service_config in config.iteritems():
				resp = requests.get(service_config['status_url'])
				color = resp.json()['color']
				config[service]['comms'] = decode_color(color)
				print color
			time.sleep(30)
	except KeyboardInterrupt:
		pass
	except Exception as e:
		logging.exception("bailing!")
	finally:
		RPIO.cleanup()
		for _, service_config in config.iteritems():
			if service_config['led']:
				servo.stop_servo(service_config['led'])

if __name__ == "__main__":
	main()
