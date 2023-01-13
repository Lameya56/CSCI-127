#Name: Lameya Mostafa
#Email: Lameya.mostafa18@myhunter.cuny.edu
#Date: September 19, 2022
#This program prints list of names
names = input("Enter a list of names, separated by semicolon: ")
separate = names.split(";")
for s in separate: 
  n= s[0]
  s= s.split(" ")
  s2 = s[1]
  name = n + "." +" "+ s2
  print(name)

