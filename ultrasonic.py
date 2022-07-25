import RPi.GPIO as gpio
import time

# gpio mode
gpio.setmode(gpio.BCM)

# set pins
TRIG = 23
ECHO = 24

gpio.setup(TRIG, gpio.OUT)
gpio.setup(ECHO, gpio.IN)


def get_distance():
    # set trigger to high
    gpio.output(TRIG, True)

    # set trigger to low
    time.sleep(0.00001)
    gpio.output(TRIG, False)

    pulse_start = time.time()
    pulse_end = time.time()

    # get start time and break the loop if it stuck
    start_time = time.time()
    # get pulse start time
    while gpio.input(ECHO) == 0:
        pulse_start = time.time()
        if (time.time() - start_time) > 2:
            break

    # get time of arrival
    while gpio.input(ECHO) == 1:
        pulse_end = time.time()
        if (time.time() - start_time) > 2:
            break

    # difference between start and arrival
    pulse_duration = pulse_end - pulse_start

    distance = (pulse_duration * 34300) / 2

    return distance

if __name__ == "__main__":
    try:
        while True:
            distance = round(get_distance(), 2)
            print(f"Distance: {distance} cm")
            time.sleep(1)

    except:
        print("Keyboard interrupt")
        gpio.cleanup()
