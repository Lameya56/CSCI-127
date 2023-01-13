#Name: Lameya Mostafa
#Email: Lameya.mostafa18@myhunter.cuny.edu
#Date: September 14, 2022
#This program prints pink eye
import turtle
t= turtle.Turtle()
turtle.colormode(255)
t.backward(100)
for i in range(0,255,10):
    t.forward(10)
    t.pensize(i)
    t.color(i,0,i)
for i in range(255,0,-10):
    t.forward(10)
    t.pensize(i)
    t.color(i,0,i)