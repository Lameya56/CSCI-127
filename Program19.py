#Name: Lameya Mostafa
#Email: Lameya.mostafa18@myhunter.cuny.edu
#Date: September 29, 2022
#This program converts between cm and feet/inches

print("(a) convert centimeters to feet\n(b) convert centimeters to feet and inches\n(c) convert feet and inches to centimeters")
user_choice = input("Enter a or b or c: ")
if user_choice == "a":
    cm = float(input("Enter height in centimeters: "))
    feet= cm/30.48
    feet = round(feet,2)
    print("height is "+ str(feet) + " feet")
elif user_choice =="b":
    cm = float(input("Enter height in centimeters: "))
    feet= int(cm/30.48)
    inches = round(int(((cm-(feet*30.49))/2.54)))
    print("height is "+ str(feet) + " feet and " + str(inches) + " inches" )
elif user_choice == "c":
    feet_str, inches_str = input("Enter height in feet and inches, separated by a space: ").split()
    #convert feet_str to an int using 
    feet = int(feet_str)* 30.48
    inches= int(inches_str)*2.54
    final= round(feet+inches)
    print("height is "+ str(final) + " cm")
else:
    print("Wrong choice, please enter only a or b or c.")


