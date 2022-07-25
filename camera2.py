import RPi.GPIO as gpio
import time
import cv2

gpio.setmode(gpio.BCM)
gpio.setup(20, gpio.OUT)
gpio.setup(26, gpio.OUT)

print('start')

cam = cv2.VideoCapture(0)
cam.set(3, 640)
cam.set(4, 480)

while True:

    ret, frame = cam.read()

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    if cv2.waitKey(50) & 0xFF == ord('a'):
        print('left')
        gpio.output(20, True)
        cv2.waitKey(50)
        gpio.output(20, False)
    if cv2.waitKey(50) & 0xFF == ord('d'):
        print('right')
        gpio.output(26, True)
        cv2.waitKey(50)
        gpio.output(26, False)

    cv2.imshow('', frame)


cam.release()
cv2.destroyAllWindows()
gpio.cleanup()
