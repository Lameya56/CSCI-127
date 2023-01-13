#Name: Lameya Mostafa
#Email: Lameya.mostafa18@myhunter.cuny.edu
#Date: October 18, 2022
#This program prints liquid price

def computePrice(liquid,size):
    if liquid=="coffee":
        if size=="small":
            print(size + " size "+liquid+ ": 2.5")
            return 2.5
        elif size=="medium":
            print(size + " size "+liquid+ ": 2.75")
            return 2.75
        elif size=="large":
            print(size + " size "+liquid+ ": 3.00")
            return 3.00
        else:
            return -1
    elif liquid=="misto":
        if size=="small":
            print(size + " size "+liquid+ ": 3.15")
            return 3.15
        elif size== "medium":
            print(size + " size "+liquid+ ": 3.35")
            return 3.35
        elif size=="large":
            print(size + " size "+liquid+ ": 3.7")
            return 3.7
        else:
            return -1
    elif liquid== "mocha":
        if size=="small":
            print(size + " size "+liquid+ ": 3.5")
            return 3.5
        elif size=="medium":
            print(size + " size "+liquid+ ": 3.8")
            return 3.8
        elif size=="large":
            print(size + " size "+liquid+ ": 4.25")
            return 4.25
        else:
            return-1
    elif liquid=="tea":
        if size=="small":
            print(size + " size "+liquid+ ": 2.35")
            return 2.35
        elif size=="medium":
            print(size + " size "+liquid+ ": 2.45")
            return 2.45
        elif size=="large":
            print(size + " size "+liquid+ ": 2.90")
            return 2.90
        else: 
            return -1
    else:
        print(size + " size "+liquid+ ": -1")
        return -1
            
#computePrice("mocha","medium")

