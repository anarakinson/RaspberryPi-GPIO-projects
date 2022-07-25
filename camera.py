import RPi.GPIO as gpio
import time
import cv2

gpio.setmode(gpio.BCM)

gpio.setup(20, gpio.OUT)
servo1 = gpio.PWM(20, 50)

cam = cv2.VideoCapture(0)

servo1.start(0)
duty = 6.8
servo1.ChangeDutyCycle(duty)
cv2.waitKey(1)

while True:

    ret, frame = cam.read()

    cv2.imshow('', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    if cv2.waitKey(1) & 0xFF == ord('a'):
        duty += 0.3
        print(duty)
        servo1.ChangeDutyCycle(duty)
        cv2.waitKey(1)
        if duty > 12:
            duty = 12
    if cv2.waitKey(1) & 0xFF == ord('d'):
        duty -= 0.3
        servo1.ChangeDutyCycle(duty)
        cv2.waitKey(1)
        if duty < 0:
            duty - 0
time.sleep(2)

servo1.ChangeDutyCycle(6.8)
cv2.waitKey(1)



cam.release()
cv2.destroyAllWindows()

servo1.stop()
gpio.cleanup()
print("end")
