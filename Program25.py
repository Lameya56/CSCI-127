#Name: Lameya Mostafa
#Email: Lameya.mostafa18@myhunter.cuny.edu
#Date: September 29, 2022
#This program prints binary to decimal
binary = input("Enter a string with 0 or 1 only: ")
num = 0
base = 2
weight = 1
length = len(binary)
ch = ""

for i in binary[::-1]:
    ch=i
    if ch=='1':
        num+=weight
    elif ch!='0':
        print("Letter",ch,"is not allowed in binary string.")
        exit()
    weight*=base
print("num = "+str(num))
'''
#Binary to decimal 
decimal = 0
for digit in binary:
    decimal = decimal*2 + int(digit)   
print ("num = " + str(decimal))
'''

