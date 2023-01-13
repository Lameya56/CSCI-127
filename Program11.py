#Name: Lameya Mostafa
#Email: Lameya.mostafa18@myhunter.cuny.edu
#Date: September 13, 2022
#This program prints cipher
'''
#Why doesn't this work??
import turtle
t = turtle.Turtle()
turtle.colormode(255)
for j in range(2):
    t.pendown()
    for i in range(0,250,10):
        t.pensize(i)
        t.color(0,i,i)
        t.forward(10)
        
    t.penup()
    t.backward(260)
    t.left(90)   
t.right(260)
'''
#this workss!
import turtle
turtle.colormode(255)
t = turtle.Turtle()

for  i in range(2):
  t.pendown()
  for j in range(0,255,10):
    t.pensize(j)
    t.color(0,j,j)
    t.forward(10)

  t.penup()
  t.backward(260)
  t.left(90)

t.right(90)  

