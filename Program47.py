#Name: Lameya Mostafa
#Email: Lameya.mostafa18@myhunter.cuny.edu
#Date: November 1,2022
#This program prints perfect number


start=0
end=100
print("Pick an integer in [0, 100] in your mind.")
def guessGame(start,end):
    guess= int(start+end)//2
    numGuesses= 1
    print("Guess "+ str(numGuesses)+ ":"+ " is it " +str(guess)+" ?" )
    print("1: too small   2: too big   3: just right")
    feedback = int(input("Enter choice 1-3: "))

    while feedback != 1 and feedback !=2 and feedback !=3: 
        feedback = int(input("Enter choice 1-3: "))
    if feedback==1:
        start= int(guess+1)
        guessGame(start,end)
    

    if feedback==2:
        end= int(guess-1)
        guessGame(start,end)
    
    if feedback==3:
        print("Congratulations! the value is "+ str(guess))
guessGame(start,end)
        

