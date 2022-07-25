import RPi.GPIO as gpio
import time
import cv2

gpio.setmode(gpio.BCM)
LED_PIN = 21

def lighter_on():
    gpio.setup(LED_PIN, gpio.OUT)

    print('start')

    time.sleep(1)
    gpio.output(21, True)


if __name__ == "__main__":
    try:
        lighter_on()
        while True:
            pass
    except:
        print("Keyboard interrupt")
        gpio.output(LED_PIN, False)
        gpio.cleanup()
