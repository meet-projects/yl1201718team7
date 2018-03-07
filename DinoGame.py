from turtle import *
import time
from DinoClass import Dino
from Map import Map

ht()
window = Screen()
window.setup(width = 544, height = 550)

SCREEN_WIDTH = int(getcanvas().winfo_width() / 2)
SCREEN_HEIGHT = int(getcanvas().winfo_height() / 2)

score = clone()
score.pu()
score.ht()
score.color(0.3, 0.3, 0.3)
score.goto(SCREEN_WIDTH - 50, SCREEN_HEIGHT - 30)

FLOOR_INITIAL_VELOCITY = -2
CLOUD_INITIAL_VELOCITY = -3
MOON_INITIAL_VELOCITY = -1
BIRD_INITIAL_VELOCITY = -3

tracer(0)
ht()

#Ground
ground = Map(0, -17, 0, "Images/ground.gif")

#Player
player = Dino(0, 0, 40, "Images/Dinasour_Idle.gif", 43, 46, "Images/Dinasour_Run_1.gif", "Images/Dinasour_Run_2.gif", "Images/Dinasour_Idle.gif", "Images/Dinasour_Dead.gif", "Images/Dinasour_Duck_1.gif", "Images/Dinasour_Duck_2.gif")

#Map Objects
map = []
cactus1 = Map(SCREEN_WIDTH , -5, FLOOR_INITIAL_VELOCITY, "Images/Cactus1.gif", 51, 45)

map.append(cactus1)

cactus2 = Map(SCREEN_WIDTH * 1.5, -8, FLOOR_INITIAL_VELOCITY, "Images/Cactus2.gif", 33, 32)
map.append(cactus2)

cactus3 = Map(SCREEN_WIDTH * 2, 0, FLOOR_INITIAL_VELOCITY,"Images/Cactus3.gif", 15, 25)
map.append(cactus3)

cactus4 = Map(SCREEN_WIDTH * 2.5, -5, FLOOR_INITIAL_VELOCITY,"Images/Cactus4.gif", 19, 35)
map.append(cactus4)

#bird = Map(SCREEN_WIDTH * 4.5, 75, BIRD_INITIAL_VELOCITY, "Images/Bird_1.gif", "Images/Cactus2.gif", 43, 33)
#map.append(bird)

moon = Map(SCREEN_WIDTH, 200, MOON_INITIAL_VELOCITY, "Images/Moon.gif", 22, 46)
map.append(moon)

cloud = Map(SCREEN_WIDTH, 150, CLOUD_INITIAL_VELOCITY,"Images/Cloud.gif", 53, 20)
map.append(cloud)

game_over = Map(-25, 100, 0, "Images/Game_Over.gif")
game_over.ht()
 
player.move()
isOver = False
#bird.moveBird()
while (True):
	currentTime = int(time.clock())

	onkeypress(player.jump, "space")
	onkeypress(player.duck, "Down")
	listen()

	for i in map:
		i.moveMap(map)
		isOver = i.playerCollision(map, player)

	score.clear()
	score.write(int(time.clock() *  16), False, "left", font=("Comic Sans MS", 15, "normal"))

	if isOver == True:
		time.sleep(1)
		exit()

	getscreen().update()
	time.sleep(0.0077)

mainloop()