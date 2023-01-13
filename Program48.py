#Name: Lameya Mostafa
#Email: Lameya.mostafa18@myhunter.cuny.edu
#Date: November 1,2022
#This program prints random integer

import random
def integer():
    ui=int(input("Enter only 1-6: "))
    while ui !=1 and ui !=2 and ui != 3 and ui !=4 and ui!= 5 and ui!= 6:
        print("Input needs to be in 1-6. Re-enter:")
        ui=int(input("Enter only 1-6: "))
    return ui
def guessGame():
    user= integer()
    computer= random.randint(1,7)
    print("user: "+ str(user))
    print("computer: "+ str(computer))
    if user == computer:
        print("draw")
    elif user+computer == 3 or user+computer==6 or user+computer==7 or user+computer==8:
        print("user wins")
    else:
        print("computer wins")
def main():
    guessGame()
if __name__=="__main__":
    main()



