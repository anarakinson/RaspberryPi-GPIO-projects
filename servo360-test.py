import RPi.GPIO as gpio
import time
import numpy as np

gpio.setmode(gpio.BCM)

gpio.setup(26, gpio.OUT)
servo1 = gpio.PWM(26, 50)

servo1.start(0)
print("waiting for 1 sec")
time.sleep(1)

print("rotating 180 degrees in 10 steps")

gpio.output(26, True)
servo1.ChangeDutyCycle(6)
gpio.output(26, False)
time.sleep(0.01)
servo1.ChangeDutyCycle(0)
time.sleep(5)

print(7.5)
gpio.output(26, True)
servo1.ChangeDutyCycle(8)
gpio.output(26, False)
time.sleep(0.008)
servo1.ChangeDutyCycle(0)
time.sleep(5)

#for i in np.arange(0, 100, 1):
#    print(i)
#    servo1.ChangeDutyCycle(i)
#    time.sleep(0.01)
#    servo1.ChangeDutyCycle(0)
#    time.sleep(2)


servo1.stop()
gpio.cleanup()
print("end")
