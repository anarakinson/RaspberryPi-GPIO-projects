import RPi.GPIO as gpio
import time
import cv2

gpio.setmode(gpio.BCM)
gpio.setup(21, gpio.OUT)

print('start')

while True:
    time.sleep(2)
    for i in [0.7, 0.7, 0.7, 1.5, 1.5, 1.5, 0.7, 0.7, 0.7]:
        time.sleep(1)
        gpio.output(21, True)
        time.sleep(i)
        gpio.output(21, False)
        if 0xFF == ord('q'):
            break
