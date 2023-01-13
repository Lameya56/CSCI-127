#Name: Lameya Mostafa
#Email: Lameya.mostafa18@myhunter.cuny.edu
#Date: October 31, 2022
#This program draws flower using function

import turtle
#wn= turtle.Screen()

def petal(color, angle):
    turtle.colormode(255)
    t = turtle.Turtle(visible=False)
    t.left(angle)
    for i in range(0,255,10):
        t.forward(10)		#Move forward
        t.pensize(i)		#Set the drawing size to be i (larger each time)
    if color=="red":
        t.pencolor(i,0,0)
    elif color=="blue":
        t.pencolor(0,0,i)
    elif color=="green":
        t.pencolor(0,i,0)
    elif color=="cyan":
        t.pencolor(0,i,i)
    elif color=="pink":
        t.pencolor(i,0,i)
    else:
        t.pencolor(0,i,0)
        
def flower(color, numPetals):
    angle=0
    for j in range(numPetals):
        petal(color,angle)
        angle+=360/numPetals
def main():
    flower("green",9)
#wn.exitonclick()