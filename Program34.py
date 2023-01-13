#Name: Lameya Mostafa
#Email: Lameya.mostafa18@myhunter.cuny.edu
#Date: October 18, 2022
#This program cuts image

import matplotlib.pyplot as plt
import numpy as np

print("Enter 1 to get upper right corner \nEnter 2 to get middle portion")
choice = input("Your choice: ")
if choice=="1":
    img= plt.imread(input("Enter input file name: "))
    output= input("Enter output file name: ")
    height= img.shape[0]
    width=img.shape[1]
    img2= img[:height//2,width//2:]
    #plt.imshow(img2)
    plt.imsave(output,img2)
    #plt.show()
elif choice=="2":
    img= plt.imread(input("Enter input file name: "))
    output= input("Enter output file name: ")
    height= img.shape[0]
    width=img.shape[1]
    img2= img[height//4: 3*height//4,width//4:3*width//4]
    #plt.imshow(img2)
    plt.imsave(output,img2)
    #plt.show()
else: 
    print("wrong choice")


