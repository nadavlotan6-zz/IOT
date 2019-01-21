import RPi.GPIO as GPIO
import time
import random

red_btn = 6
yellow_btn = 17
green_btn = 27
blue_btn = 5

def main():
	init_gpio()
	while True:
		if GPIO.input(red_btn) == GPIO.HIGH :
			print("Red button was pressed!")
		elif GPIO.input(yellow_btn) == GPIO.HIGH :
			print("Yellow button was pressed!")
		elif GPIO.input(green_btn) == GPIO.HIGH :
			print("Green button was pressed!")
		elif GPIO.input(blue_btn) == GPIO.HIGH :
			print("Blue button was pressed!")

def init_gpio() :
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(red_btn, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(yellow_btn, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(green_btn, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(blue_btn, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

if __name__ == "__main__":
    main()