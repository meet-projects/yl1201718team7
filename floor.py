#imports
from turtle import *
from barrel import Barrel
import time
from player import *
from ladder import Ladder
import math
from enemy import *

clearscreen()
clear()

enemy = Enemy()
yposi = -301
for i in range(2):
	ladder = Ladder(510,yposi + 10)
	yposi = -101
yposi = -201
for i in range(2):
	ladder2 = Ladder(-505,yposi + 10)
	yposi = -1

bgcolor("lightgray")
player = Player()
tracer(0)
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
BARREL_AMOUNT = 3
current_time = 0
position_list = []
FPS = 1/80#frames per second
barrel_list = []
start_pos = -SCREEN_HEIGHT/2+50
setup(SCREEN_WIDTH,SCREEN_HEIGHT)
number_of_floors = 5
floor_list = []
floor_min_height = -SCREEN_HEIGHT/2 + 0
current_floor_height = floor_min_height
left_edge = -SCREEN_WIDTH/2 + 50
right_edge = SCREEN_WIDTH/2 - 50
ladder_list = []

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
		self.color("black")
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
direction = "upright"
def upright():
	global direction
	direction = "upright"
def downright():
	global direction
	direction = "downright"
def upleft():
	global direction
	direction = "upleft"
def downleft():
	global direction
	direction = "downleft"
def up():
	global direction, current_time
	direction = "up"
is_right = True

def my_f(x):
	return 0.041*x + 77.96
def r_f(x):
	return -0.041*x + 77.96
def move_player():
	global direction, position_list, is_right
	if is_right == True:
		onkey(upright, "Right")
		onkey(downleft, "Left")
		onkey(up,"Up")

		listen()
	if is_right == False:
		onkey(up,"Up")

		onkey(upleft, "Left")
		onkey(downright, "Right")
		onkey(up,"Up")

		listen()
	current_x = player.xcor()
	if direction == "upright":
		player.goto(current_x + player.speed,my_f(current_x + player.speed) - player.offset)
		
		print(str(player.xcor())+","+str(player.ycor()))
		position_list.append(player.ycor())
	if direction == "downleft":
		player.goto(current_x - player.speed,my_f(current_x - player.speed) - player.offset)
		print(str(player.xcor())+","+str(player.ycor()))

		position_list.append(player.ycor())
	if direction == "upleft":
		player.goto(current_x - player.speed,r_f(current_x - player.speed) - player.offset)
		print(str(player.xcor())+","+str(player.ycor()))

		position_list.append(player.ycor())
	if direction == "downright":
		player.goto(current_x + player.speed,r_f(current_x + player.speed) - player.offset)
		print(str(player.xcor())+","+str(player.ycor()))

		position_list.append(player.ycor())	
	if direction == "up":
		jumpH = 55
		#first ladder's pos
		if player.xcor() >502 and player.xcor() < 550 and player.ycor() < -299 and player.ycor() > -303:
			jumpH = 55
			player.offset -= 100
			is_right = False

			print(is_right)
		#second ladder's pos
		elif player.xcor() <-495 and player.xcor() > -525 and player.ycor() < -191 and player.ycor() > -211:
			jumpH = 55
			player.offset -= 100

			is_right = True
			print(is_right)
		#third ladder
		elif player.xcor() >497 and player.xcor() < 550 and player.ycor() < -96 and player.ycor() > -107:
			jumpH = 55
			player.offset -= 100
			is_right = False

			print(is_right)
		#forth ladder
		elif player.xcor() <-495 and player.xcor() > -525 and player.ycor() <  8 and player.ycor() > -8:
			jumpH = 55
			player.offset -= 100

			is_right = True

			print(is_right)
		else:
			jumpH = 42
		ypos = position_list[-1] + jumpH
		player.goto(current_x, ypos)

	if player.xcor() >= 470 and player.ycor() >= 90:
		win()



def win():
	clearscreen()
	write("you won", move=False, align="center", font=("Arial", 80, "normal"))
	time.sleep(2)
	clear()
	import menu
		

def lose():
	global barrel_list
	clear()
	for i in barrel_list:
		i.ht()
		i.clear()
	for i in floor_list:
		i.clear()
		i.ht()
	player.ht()
	player.clear()
	ht()
	pu()
	goto(0,0)
	pd()
	color("white")
	write("you lost!", move=False, align="center", font=("Arial", 80, "normal"))
	time.sleep(3)
	import menu
def check_col():
	for i in barrel_list:
		if math.fabs(i.xcor() - player.xcor()) < 10 and math.fabs(i.ycor() - player.ycor()) < 10:
			lose()

offset = 3
last_created = time.time() - offset
created = 0

while True: # THE GAME LOOP, EACH ITERATION = 1 FRAME

	check_col()
	move_player()

	if created < BARREL_AMOUNT and time.time() - last_created > offset:
		barrel1 = Barrel(False)
		barrel_list.append(barrel1)
		created +=1
		last_created = time.time()
	for i in barrel_list:
		i.crawl()

	update()

	time.sleep(FPS)#FPS(frames per second)

mainloop()