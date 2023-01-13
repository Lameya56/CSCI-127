#Name: Lameya Mostafa
#Email: Lameya.mostafa18@myhunter.cuny.edu
#Date: October 17, 2022
#This program prints greetings by the hour

time= int(input("Enter hour (in 24 hour time):  "))
if time <12:
    print("Good Morning")
elif time >= 12 and time< 17:
    print("Good Afternoon")
else:
    print("Good Evening")