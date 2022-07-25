import RPi.GPIO as gpio
import time
import cv2

gpio.setmode(gpio.BCM)
gpio.setup(20, gpio.OUT)
gpio.setup(26, gpio.OUT)

print('start')

while True:
    print('left')
    gpio.output(20, True)
    time.sleep(1.5)
    gpio.output(20, False)
    print('right')
    gpio.output(26, True)
    time.sleep(1.5)
    gpio.output(26, False)
    break
gpio.cleanup()
