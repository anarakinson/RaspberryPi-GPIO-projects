#!/usr/bin/python3
import RPi.GPIO as GPIO
import pigpio
import time
import subprocess

# start pigpiod
# subprocess.run(["sudo", "pigpiod"])
 
servo = 26
 
# more info at http://abyz.me.uk/rpi/pigpio/python.html#set_servo_pulsewidth
 
pwm = pigpio.pi() 
pwm.set_mode(servo, pigpio.OUTPUT)

pwm.set_PWM_frequency( servo, 50 )


#print("rotate 180 degree")
#for i in range(1300, 1601, 5):
#    pwm.set_servo_pulsewidth( servo, i )
#    time.sleep(0.01)

print("return to 90 degree")
pwm.set_servo_pulsewidth(servo, 1400)
time.sleep(1)

print("return to 90 degree")
pwm.set_servo_pulsewidth(servo, 1600)
time.sleep(1)


# turning off servo
print("turning off")
pwm.set_PWM_dutycycle(servo, 0)
pwm.set_PWM_frequency( servo, 0 )
