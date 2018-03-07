from turtle import *
SCREEN_WIDTH = 1280
right_edge = SCREEN_WIDTH/2 - 50
shapeSize = 40
newSize = shapeSize/2 - 5
class Enemy(Turtle):
	def __init__(self):
		Turtle.__init__(self)
		register_shape("enemy.gif")
		self.pu()
		self.shape("enemy.gif")
		self.goto(right_edge - 10 ,95 + newSize)