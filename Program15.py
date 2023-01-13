#Name: Lameya Mostafa
#Email: Lameya.mostafa18@myhunter.cuny.edu
#Date: September 15, 2022
#This program prints words in k shape
name = input("Enter a phrase: ")
split = name.split(" ")
for i in range(len(split)):
  if i <= 0:
    print(" ".join(split))
  else:
    print(" ".join(split[:-i]))
for j in range(len(split)):
    if j<= 0:
        continue
    else:
        print(" ".join(split[:j+1]))