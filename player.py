
from turtle import *
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
SHAPE_X = 30
SHAPE_Y = 30
#class begin
class Player(Turtle):
	def __init__(self):
		Turtle.__init__(self)
		self.pu()
		self.ht()
		self.x = -SCREEN_WIDTH/2 + SHAPE_X + 300
		self.y = 0.041*self.x + 77.96
		register_shape("player.gif")
		self.shape("player.gif")
		self.offset = 400
		self.goto(self.x,self.y- self.offset)
		self.st()
		self.speed = 0.4
	def direction(self):
		if self.offset%8 == 0:
			return True
		else:
			return False
		
