import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)
gpio.setup(21, gpio.IN, pull_up_down=gpio.PUD_DOWN)


while True:
    time.sleep(2)
    print(float(gpio.input(21)))
