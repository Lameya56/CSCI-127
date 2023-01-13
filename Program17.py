#Name: Lameya Mostafa
#Email: Lameya.mostafa18@myhunter.cuny.edu
#Date: September 29, 2022
#This program draws letter T
import numpy as np
import matplotlib.pyplot as plt
file_name = input(" Enter output file name: ")
img= np.empty((30,30,3))
img[:,:,0] = 1
img[:,:,1]= 1
img[:,:,2]=0
#the horizontal line
img[5:8,5:25,2]=1
img[5:8,5:25,0]=0
img[5:8,5:25,1]=0
#The vertical line
img[8:25,13:16,1]=1
img[8:25,13:16,0]=0
img[8:25,13:16,2]=0

#plt.imshow(img)
#plt.show()
plt.imsave(file_name,img)

