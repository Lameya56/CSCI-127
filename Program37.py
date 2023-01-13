#Name: Lameya Mostafa
#Email: Lameya.mostafa18@myhunter.cuny.edu
#Date: October 18, 2022
#This program draws flower in a recursive function

import turtle
t= turtle.Turtle

def flowerRecursion(t, n):
   if n > 0:
      #draw one petal
       t.forward(100)
       t.left(105)
       t.forward(52)
       t.left(105) 
       t.forward(100)
      #prepare to move direction to draw next petal
       t.right(170)
       flowerRecursion(t,n-1)

flowerRecursion(t,10)