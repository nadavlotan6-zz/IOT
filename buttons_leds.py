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
		if GPIO.input(red_btn) == GPIO.HIGH :
			flash_led(red_led)
		elif GPIO.input(yellow_btn) == GPIO.HIGH :
			flash_led(yellow_led)
		elif GPIO.input(green_btn) == GPIO.HIGH :
			flash_led(green_led)
		elif GPIO.input(blue_btn) == GPIO.HIGH :
			flash_led(blue_led)

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


def flash_led(led) :
        GPIO.output(led, GPIO.HIGH)
        time.sleep(2)
        GPIO.output(led, GPIO.LOW)



# sets main to start automatically
if __name__ == "__main__":
    main()