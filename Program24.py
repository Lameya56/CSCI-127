#Name: Lameya Mostafa
#Email: Lameya.mostafa18@myhunter.cuny.edu
#Date: October 3, 2022
#This program prints words ending with a or b

list= input("Enter a list of words, separated by a space: ")
no_of_words= len(list.split())
words= list.split()
print("number of words: " +str(no_of_words))
count= 0
for word in words:
    if word[-1]=="a" or word[-1]=="b":
        count+=1
print("number of words ending with a or b: " + str(count))
fraction = round((count/no_of_words),2)
print("fraction of words starting with a or b: "+ str(fraction))
