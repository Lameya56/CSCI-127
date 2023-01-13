#Name: Lameya Mostafa
#Email: Lameya.mostafa18@myhunter.cuny.edu
#Date: September 19, 2022
#This program sets red channel of an image to zero
import matplotlib.pyplot as plt
import numpy as np

inFile= input("Enter name of the input file: ")
outFile = input("Enter name of the output file: ")
img = plt.imread(inFile)    #Read in image
plt.imshow(img)               #Load image into pyplot
plt.show()                    #Show the image
img[:,:,0]=0
plt.imshow(img)
plt.show()
plt.imsave(outFile,img)   #Save the image to the outFile

