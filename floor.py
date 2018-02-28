#imports
from turtle import *
from barrel import Barrel
import time

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
start_pos = -SCREEN_HEIGHT/2+50
setup(SCREEN_WIDTH,SCREEN_HEIGHT)
number_of_floors = 5
floor_list = []
floor_min_height = -SCREEN_HEIGHT/2 + 0
current_floor_height = floor_min_height
left_edge = -SCREEN_WIDTH/2 + 50
right_edge = SCREEN_WIDTH/2 - 50
goto(left_edge + 75,0)

begin_poly()

pd()
goto(right_edge + 50,-50)
end_poly()
left_side_shape = get_poly()

clear()
goto(right_edge - 75,0)

begin_poly() 
pd()
goto(left_edge - 50,-50)
pu()
end_poly()

right_side_shape = get_poly()
clear()
register_shape("right_floor", right_side_shape)
register_shape("left_floor", left_side_shape)
class Floor(Turtle):
	def __init__(self,y):
		Turtle.__init__(self)
		self.pu()
		self.y = y

		self.goto(0,y)
for i in range(number_of_floors):
	
	if i%2 == 0:
		floor = Floor(current_floor_height)
		floor.right(90)
		floor.shape("right_floor")
		floor_list.append(floor)
	else:
		floor = Floor(current_floor_height)
		floor.right(90)
		floor.shape("left_floor")
		floor_list.append(floor)
	current_floor_height += 100
print(floor.y)

barrel1 = Barrel(False)
barrel1.crawl()


mainloop()
