import RPi.GPIO as GPIO
import time
import random

red_led = 26
yellow_led = 21
green_led = 20
blue_led = 19

lights = [red_led, yellow_led, green_led, blue_led]

def flash_led(led) :
        GPIO.output(led, GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(led, GPIO.LOW)

def main():
        init_gpio()
        flash_led(red_led)
        flash_led(yellow_led)
        flash_led(green_led)
        flash_led(blue_led)

def init_gpio() :
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(red_led, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(yellow_led, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(green_led, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(blue_led, GPIO.OUT, initial=GPIO.LOW)
        # GPIO.setup(buttons, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        #for i in range(4) :
        #       GPIO.add_event_detect(buttons[i], GPIO.RISING, callback=button_callback)

if __name__ == "__main__":
    main()

