from turtle import *
import time
import random

SCREEN_WIDTH = int(getcanvas().winfo_width() / 2)
SCREEN_HEIGHT = int(getcanvas().winfo_height() / 2)

class Map(Turtle):
	def __init__(self, x, y, dx, idle, animation = "", width = 0, height = 0):
		Turtle.__init__(self)

		self.pu()
		self.x = x
		self.start_x = SCREEN_WIDTH
		self.y = y
		self.goto(self.x, self.y)

		self.width = width
		self.height = height

		self.dx = dx
		self.idle = idle
		self.animation = animation

		self.rightAnimation = False
		self.TIMER = 100

		Screen().register_shape(self.idle)
		self.shape(self.idle)

	def moveMap(self, map):
		self.x = self.x + self.dx
		self.goto(self.x, self.y)

		for i in map:
			if self.x < -SCREEN_WIDTH and self.start_x > ((i.x + (i.width / 2)) + 300):
				self.x = SCREEN_WIDTH


	def moveBird(self):
		if self.rightAnimation == False:
			self.shape(self.idle)
			self.rightAnimation = True
		else:
			self.shape(self.animation)
			self.rightAnimation = False

		ontimer(self.moveBird, self.TIMER)

	def playerCollision(self, map, player):
		for i in map:
			if player.x - player.width / 2 < i.x + i.width / 2 and player.x + player.width / 2 > i.x - i.width / 2 and player.y + player.height / 2 > i.y - i.height / 2 and player.y - player.height / 2 < i.y + i.height / 2:
				return True

		return False