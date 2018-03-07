from turtle import *
class Ladder(Turtle):
	def __init__(self,x,y):
		Turtle.__init__(self)
		self.x = x
		self.y = y
		self.pu()
		register_shape("ladder.gif")
		self.shape("ladder.gif")
		self.goto(self.x,self.y)