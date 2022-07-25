#!/usr/bin/python3
import RPi.GPIO as GPIO
import pigpio
import time
import subprocess
import argparse



def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--angle", help="set angle", default="90")
    parser.add_argument("-p", "--pin", help="set servo pin", default="26")
    args = parser.parse_args()
    return args

def main():
    # start pigpiod
    # subprocess.run(["sudo", "pigpiod"])
 
    args = parse_args()

    servo = int(args.pin)
    angle = int(args.angle)

    if angle > 180:
        angle = 180
    if angle  < 0:
        angle = 0
    print(angle)
    angle = ((angle / 90) * 1000) + 500
 
    # more info at http://abyz.me.uk/rpi/pigpio/python.html#set_servo_pulsewidth
 
    pwm = pigpio.pi() 
    pwm.set_mode(servo, pigpio.OUTPUT)

    pwm.set_PWM_frequency( servo, 50 )


#    for i in range(500, 2501, 5):
#        #print(f"freqency - {i}")
#        pwm.set_servo_pulsewidth( servo, i )
#        time.sleep(0.01)

#    print("return to 90 degree")
    pwm.set_servo_pulsewidth(servo, angle)
    time.sleep(1)

    # turning off servo
    print("turning off")
    pwm.set_PWM_dutycycle(servo, 0)
    pwm.set_PWM_frequency( servo, 0 )

if __name__ == "__main__":
    main()
