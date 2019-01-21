import RPi.GPIO as GPIO
import time
import random
import wiringpi

c_note = 261.6256
d_note = 293.6648
e_note = 329.6276
f_note = 349.2282

red_btn = 6
yellow_btn = 17
green_btn = 27
blue_btn = 5

red_led = 26
yellow_led = 21
green_led = 20
blue_led = 19

speaker = 25

def main():
	init_gpio()
	while True:
        pass

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

        #init speaker
        wiringpi.wiringPiSetupGpio()
        wiringpi.softToneCreate(speaker)


def make_sound(sound) :
    wiringpi.softToneWrite(speaker, sound)

# flash a led with 'led' = gpioPin
def flash_led(led) :
        GPIO.output(led, GPIO.HIGH)
        time.sleep(0.2)
        GPIO.output(led, GPIO.LOW)

# events
def red_button_callback(channel) :
    flash_led(red_led)
    make_sound(c_note)

def yellow_button_callback(channel) :
    flash_led(yellow_led)
    make_sound(d_note)

def green_button_callback(channel) :
    flash_led(green_led)
    make_sound(e_note)

def blue_button_callback(channel) :
    flash_led(blue_led)
    make_sound(f_note)

# sets main to start automatically
if __name__ == "__main__":
    main()