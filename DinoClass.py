from turtle import *

class Dino(Turtle):
	def __init__(self, x, y, dy, idle, width, height, firstMove, secondMove, jumpImage, dead, firstDuck, secondDuck):
		Turtle.__init__(self)

		self.pu()
		self.x = x
		self.y = y
		self.start_y = self.y
		self.dy = dy
		self.start_dy = self.dy
		self.gravity = 10
		self.idle = idle
		self.firstMove = firstMove
		self.secondMove = secondMove
		self.jumpImage = jumpImage
		self.dead = dead
		self.firstDuck = firstDuck
		self.secondDuck = secondDuck

		self.width = width
		self.height = height

		self.rightAnimation = False
		self.isJump = False
		self.TIMER = 100

		Screen().register_shape(self.idle)
		Screen().register_shape(self.firstMove)
		Screen().register_shape(self.secondMove)
		Screen().register_shape(self.jumpImage)
		Screen().register_shape(self.dead)
		Screen().register_shape(self.firstDuck)
		Screen().register_shape(self.secondDuck)
		self.shape(self.idle)


	def jump(self):
		self.isJump = True
		self.shape(self.idle)
		self.y = self.y + self.dy 
		self.dy = self.dy - self.gravity
		self.goto(self.x, self.y)

		if self.y > self.start_y:
			ontimer(self.jump, 100)
		else:
			self.dy = self.start_dy
			self.isJump = False

	def move(self):
		if self.isJump == False:
			if self.rightAnimation == False:
				self.shape(self.firstMove)
				self.rightAnimation = True
			else:
				self.shape(self.secondMove)
				self.rightAnimation = False

		ontimer(self.move, self.TIMER)

	def duck(self):
		print("duck")