from turtle import *
clearscreen()
clear()
ht()
setup(1280,720)
bgcolor("black")

writer = clone()
writer.color("white")
writer.ht()
writer.pu()
writer.goto(0,100)
	
writer.pd()
writer.write("*donkey kong", move=False, align="center", font=("lklug", 80, "normal"))
writer.pu()
writer.goto(0,0)
writer.pd()
writer.write("*by Noam, Dan, Bassel, Adriana and Wadi", move=False, align="center", font=("DejaVuSansMono", 40, "normal"))
writer.pu()
writer.goto(0,-100)
writer.pd()
writer.write("*press 1 to start a Donkey Kong game", move=False, align="center", font=("DejaVuSansMono", 30, "normal"))
writer.pu()
writer.goto(0,-200)
writer.pd()
writer.write("*press 2 to start a T-Rex Game", move=False, align="center", font=("DejaVuSansMono", 30, "normal"))
# writer.pu()
# writer.goto(0,-300)
# writer.pd()
# writer.write("*press 1 to start a game", move=False, align="center", font=("DejaVuSansMono", 30, "normal"))
def donkey():

	import floor.py
def dino():
	clearscreen()
	writer.clear()
	clear()
	import DinoGame
# def pong():
# 	import ping
onkey(donkey,"1")
onkey(dino,"2")
onkey(ping,"3")
listen()
mainloop()