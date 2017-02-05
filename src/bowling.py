#!/usr/bin/env/python3
import math
import pygame
import sys
import engine
from .comm import Comm
import time
from events import NEW_FRAME, CONTINUE_FRAME, GAME_END

PIN_LOCATIONS = [
[720,30],		#pin 1
[730.4,24],		#pin 2
[730.4,36],		#pin 3
[740.8,18],		#pin 4
[740.8,30],		#pin 5
[740.8,42],		#pin 6
[751.2,12],		#pin 7
[751.2,24], 	#pin 8
[751.2,36],		#pin 9
[751.2,48] 		#pin 10
]

def main():
	print("Not for human consumption. Please evacuate the premises.")

if __name__ == '__main__':
	main()



class BowlingGame: #@todo(bumsik): add a socket and eventlistener to get rolls from the server
	def __init__(self):
		# Connect server
		self.comm = Comm(host="ec2-52-23-213-20.compute-1.amazonaws.com", on_change=lambda: None)
		# wait for 3 second. To connect things
		time.sleep(3)

		# Init game
		pygame.init

		#load images
		pin_images = [pygame.image.load('../assets/pin{}.png'.format(i)).convert() for i in [90,70,40,0]]
		ball_image = pygame.image.load('../assets/ball.png').convert()
		lane_image = pygame.image.load('../assets/lane.png').convert()

		game_window = pygame.display.set_mode((800, 600))

		ball = engine.Ball()
		reset_pins()
		while True: # main game loop
			for event in pygame.event.get():
				if event.type == QUIT:
					pygame.quit()
					sys.exit()

				if event.type == NEW_FRAME #@todo(jamie) have the scorer create a NEW_FRAME event after each frame
					reset_pins()
					throw_ball(wait_for_server())

				if event.type == CONTINUE_FRAME
					throw_ball(wait_for_server())

				if event.type == GAME_END:
					pass #what it should actually do @todo(aaron):
							#display text saying throw another ball to restart the game
							#create a NEW_FRAME event  

	def reset_pins():
		self.pins = []
		for i in range(10):
			y_pos = PIN_LOCATIONS[i][0]
			x_pos = PIN_LOCATIONS[i][0]
			self.pins.append(engine.Pin(x_pos, y_pos))
		#@todo(aaron): add something to reset the y_bounds
		#@todo(aaron): figure out how 

	def throw_ball(x_force, y_force):
		'''
		@params:
			x_force is a real number
			y_force is a real number
		'''
			pass #@todo(aaron) code this

	def is_on_screen(Actor):
		'''
		@params:
			Actor is an actor that the game needs to keep track of

		returns true if Actor is in the part of the bowling alley that we are rendering.
		'''
		if 

	def wait_for_server(self):
		'''
		Waits until the server sends data, then returns an interpretation of the data.
		
		returns two things
		x_force, y_force

		note: if we can't make it work, then use a two member tuple.
		'''
		pass #@todo(aaron) code this
		while True:
			for dev_id in self.comm.get_remotes():
				# 1. get data
				print("wait for " + str(dev_id) + "...")
				data = self.comm.get_data_wait(dev_id)
				print("Data taken: " + str(data))
				# 2. plot
				self.comm.plot(data)
				# 3. calculate
				# FIXME: @kbumsik improve calculation of x and y. Currently only average list
				for axis in ("x", "y"):
					data[axis] = sum(data[axis]) / len(data[axis])
				yield (data["x"], data["y"])
		pass

	def render_lane():
		'''
		implement this LAST
		@todo(aaron)
		'''
		pass



#notes from aaron http://inventwithpython.com/pygame/chapter2.html
#http://inventwithpython.com/pygame/chapter3.html

#wake me up at 8am i'mm be in quiet room
#dow hat you can until then
#jamie google 'bowling score kata' it will HELP YOU
#bumsik you're a great dev, it's been awesome working with you
#will you're awesome, if we were gays we'd probably be married by now or smth (no homo)