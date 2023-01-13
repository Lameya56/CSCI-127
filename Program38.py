#Name: Lameya Mostafa
#Email: Lameya.mostafa18@myhunter.cuny.edu
#Date: October 18, 2022
#This program draws pentagon and nested pentagon in recursion

import math
import turtle
t= turtle.Turtle()

#recursive function to draw a pantegon
def drawPantegon(t, length, numEdges):
   if numEdges > 0:
      t.forward(length)
      t.left(72) 
      drawPantegon(t, length, numEdges-1)
#pseudocode of cornerPantegon, which draws pantegon nested in left corner.
def cornerPantegon(t, length):
   if length >= 25:
      drawPantegon(t, length, 5)
      length= length//2
      cornerPantegon(t,length)
def nestedPantegon(t, length):
    if length >= 25:
       drawPantegon( t, length, 5)
       t.forward (length/2)
       t.left(36)
       pos=t.position()
       nestedPantegon (t, length * math.sin(54/180 * math.pi))