#Name: Lameya Mostafa
#Email: Lameya.mostafa18@myhunter.cuny.edu
#Date: September 29, 2022
#This program prints blue and green stripes
import numpy as np
import matplotlib.pyplot as plt
size = int(input("Enter the size: "))
file= input("Enter output file: ")
img = np.empty((size,size,3))

for i in range(size):
    if i%2==0:
        img[:,i,0]=0
        img[:,i,1]=1
        img[:,i,2]=0
    else:
        img[:,i,0]=0
        img[:,i,1]=0
        img[:,i,2]=1
plt.imsave(file,img)
plt.imshow(img)
plt.show()