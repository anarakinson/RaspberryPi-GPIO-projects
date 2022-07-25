import RPi.GPIO as gpio
import time
import cv2

gpio.setmode(gpio.BCM)
gpio.setup(20, gpio.OUT)
gpio.setup(26, gpio.OUT)

print('start')

print('left')
gpio.output(20, True)
time.sleep(5)
gpio.output(20, False)
time.sleep(5)
print('right')
gpio.output(26, True)
time.sleep(5)
gpio.output(26, False)




gpio.cleanup()
