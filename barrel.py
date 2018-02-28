
from turtle import *
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
left_edge = -SCREEN_WIDTH/2 + 50
right_edge = SCREEN_WIDTH/2 - 50
register_shape("barrel.gif")
shapeSize = 40
newSize = shapeSize/2 - 10
class Barrel(Turtle):

	def __init__(self,is_special):

		Turtle.__init__(self)
		self.is_special = is_special

		self.x = SCREEN_WIDTH/2 -30
		self.y = 360
		self.r = 5
		self.pu()
		self.goto(right_edge + 50,95 + newSize)

		# dont forget to set the shape to the crawling shape

	def crawl(self):
		self.pu()
		self.speed(1)
		self.ht()
		self.st()
		self.shape("barrel.gif")

		self.goto(left_edge + 50,45 + newSize)
		self.goto(left_edge + 50, -5 + newSize)
		self.goto(right_edge - 50, -55 + newSize)
		self.goto(right_edge - 50, -105 + newSize)
		self.goto(left_edge + 50, -155 + newSize)
		self.goto(left_edge + 50, -205 + newSize)
		self.goto(right_edge - 50, -255 + newSize)
		self.goto(right_edge - 50, -305 + newSize)
		self.goto(left_edge + 120, -SCREEN_HEIGHT/2 + newSize)
		self.goto(left_edge, -SCREEN_HEIGHT/2 + newSize)
		self.ht()

	def next(floors,i):

		while(floors[i+1].get_y(SCREEN_WIDTH- self.crawling_shape_r) != self.ycore()):

			self.y -= 1
			self.goto(self.x,self.y)

		# dont forget to change the shape to the crawling_shape

