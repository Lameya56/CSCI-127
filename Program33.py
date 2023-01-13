#Name: Lameya Mostafa
#Email: Lameya.mostafa18@myhunter.cuny.edu
#Date: October 17, 2022
#This program define function to find out number of occurrence of a letter

def main():
    string= input("Enter a string: ")
    char= input("Enter a char: ")
    count= string.count(char)
    print("number of "+ char+ " in "+ string + " is "+ str(count))
if __name__ == "__main__":
    main()                          