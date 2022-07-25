import RPi.GPIO as gpio
import time


def get_val():
    gpio.setmode(gpio.BCM)
    gpio.setup(21, gpio.IN, pull_up_down=gpio.PUD_DOWN)


    while True:
        time.sleep(2)
        print(float(gpio.input(21)))

if __name__ == "__main__":
    try:
        main()
    except:
        gpio.cleanup()
        print("Keyboard interrupt")
