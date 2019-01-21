import RPi.GPIO as GPIO
import time
import random

red_btn = 6
yellow_btn = 17
green_btn = 27
blue_btn = 5

red_led = 26
yellow_led = 21
green_led = 20
blue_led = 19

def main():
	init_gpio()
	while True:
        print("Waiting for event")

def init_gpio() :
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)

        #buttons
        GPIO.setup(red_btn, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(yellow_btn, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(green_btn, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(blue_btn, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

        #leds
        GPIO.setup(red_led, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(yellow_led, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(green_led, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(blue_led, GPIO.OUT, initial=GPIO.LOW)

        # add events
        GPIO.add_event_detect(red_btn, GPIO.RISING, callback=red_button_callback)
        GPIO.add_event_detect(yellow_btn, GPIO.RISING, callback=yellow_button_callback)
        GPIO.add_event_detect(green_btn, GPIO.RISING, callback=green_button_callback)
        GPIO.add_event_detect(blue_btn, GPIO.RISING, callback=blue_button_callback)

# flash a led with 'led' = gpioPin
def flash_led(led) :
        GPIO.output(led, GPIO.HIGH)
        time.sleep(2)
        GPIO.output(led, GPIO.LOW)

# events
def red_button_callback(channel) :
    flash_led(red_led)

def yellow_button_callback(channel) :
    flash_led(yellow_led)

def green_button_callback(channel) :
    flash_led(green_led)

def blue_button_callback(channel) :
    flash_led(blue_led)

# sets main to start automatically
if __name__ == "__main__":
    main()