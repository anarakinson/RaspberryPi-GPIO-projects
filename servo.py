import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)

gpio.setup(19, gpio.OUT)
servo1 = gpio.PWM(19, 50)

servo1.start(0)
print("waiting for 2 sec")
time.sleep(2)

print("rotating 180 degrees in 10 steps")

duty = 2
servo1.ChangeDutyCycle(duty)
time.sleep(2)

while duty <= 12:
    servo1.ChangeDutyCycle(duty)
    time.sleep(1)
    duty += 1

time.sleep(2)

print("turning back to 0 degrees")
servo1.ChangeDutyCycle(2)
time.sleep(0.5)
servo1.ChangeDutyCycle(0)

time.sleep(1)
servo1.ChangeDutyCycle(12)
time.sleep(1)
servo1.ChangeDutyCycle(6.8)
time.sleep(1)

servo1.stop()
gpio.cleanup()
print("end")
