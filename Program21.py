#Name: Lameya Mostafa
#Email: Lameya.mostafa18@myhunter.cuny.edu
#Date: October 3, 2022
#This program loads an image, counts the number of pixels that are

#nearly white as an estimate for snow pack.

#Import the packages for images and arrays:
import matplotlib.pyplot as plt
import numpy as np

file = input("Enter file name: ")
threshold= float(input("Enter threshold: "))
ca = plt.imread(file)   #Read in image
countSnow = 0            #Number of pixels that are almost white
countPixels = 0
#t = 0.75                 #Threshold for almost white-- can adjust between 0.0 and 1.0

#For every pixel:
for i in range(ca.shape[0]):
     for j in range(ca.shape[1]):
          #Check if red, green, and blue are > t:
          if (ca[i,j,0] > threshold) and (ca[i,j,1] > threshold) and (ca[i,j,2] > threshold):
               countSnow = countSnow + 1
          if (ca[i,j,0]<=255):
               countPixels+=1

print("number of white pixels: ", countSnow)
percentage= round((countSnow/countPixels)*100,2)
print("percent of white pixels: " +str(percentage)+ " %")