import RPi.GPIO as GPIO
import time
import random
import wiringpi
from time import sleep

# saved 4 notes frequencies
c_note = 261.6256
d_note = 293.6648
e_note = 329.6276
f_note = 349.2282

# buttons gpioPins
red_btn = 6
yellow_btn = 17
green_btn = 27
blue_btn = 5

# leds gpioPins
red_led = 26
yellow_led = 21
green_led = 20
blue_led = 19

# speaker gpioPin
speaker = 25

# color, sound and buttons settings
lights = [red_led, yellow_led, green_led, blue_led]
buttons = [red_btn, yellow_btn, green_btn, blue_btn]

# sounds = {red: c_note, yellow: d_note, green: e_note, blue: f_note}
sounds = [c_note, d_note, e_note, f_note]
numbers_colors = {1: red, 2: yellow, 3: green, 4: blue}
led_dict = {"red": red_led, "yellow": yellow_led, "green":green_led, "blue":blue_led}
btn_dict = {"red": red_btn, "yellow": yellow_btn, "green":green_btn, "blue":blue_btn}

# game statistics
steps = []
players_turn = 0

# flags for game status
is_game_over = False
is_won_level = False


# main function
def main() :
	init_gpio()
	start_game()

# reset game
def reset_game() :
	is_won_level = False
	is_game_over = False
	steps = []
	GPIO.output(lights.GPIO.LOW)
	start_game()

# start the game
def start_game() :

	# flash all 4 lights
	flash_led(red_led)
	flash_led(yellow_led)
	flash_led(green_led)
	flash_led(blue_led)

	while (not is_game_over) :
		add_color_to_steps()
		display_pattern()
		player_turn()
		if is_game_over :
			game_over()
			reset_game()
		time.sleep(2)

def player_turn() :
	while True :
		pass

# deal with user's turn and valid if correct or finished game
def verify_player_selection(color) :
    if not is_game_over and not is_won_level :
        if color == steps[-1] :
	        return True
        else : return False
    else :
        return False



# add a color to the steps
def add_color_to_steps() :
	number = random.randint(1, 4)
	steps.append(numbers_colors.get(number))


''' events '''
# red event
def red_button_callback(channel) :
	if verify_player_selection("red") :
    	flash_led(red_led)
    	make_sound(c_note)
    else :
    	game_over()

# yellow event
def yellow_button_callback(channel) :
	if verify_player_selection("yellow") :
    	flash_led(yellow_led)
    	make_sound(d_note)
    else :
    	game_over()

# green event
def green_button_callback(channel) :
	if verify_player_selection("green") :
    	flash_led(green_led)
    	make_sound(e_note)
    else :
    	game_over()

# blue event
def blue_button_callback(channel) :
	if verify_player_selection("blue") :
    	flash_led(blue_led)
    	make_sound(f_note)
    else :
    	game_over()

''' events finished '''


# displays the needed colors and sounds
def display_pattern():
	for i in steps :
		index = 0
		if i == "red":
			index = 0
		elif i == "yellow" :
			index = 1 
		elif i == "green" : 
			index = 2
		else :
			index = 3
		make_sound(sounds[index])
		flash_led(led_dict.get(i))


# when game is over, flash all lights and make a sound
def game_over():
	play_sound(200)



# initialize all needed gpio pins
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


# set the speaker with a frequency and play a note
def make_sound(sound) :
	wiringpi.softToneWrite(speaker, sound)
	sleep(0.1)


# handle the flash for the button
def flash_led(led) :
        GPIO.output(led, GPIO.HIGH)
        time.sleep(2)
        GPIO.output(led, GPIO.LOW)


# sets main to start automatically
if __name__ == "__main__":
    main()


