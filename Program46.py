#Name: Lameya Mostafa
#Email: Lameya.mostafa18@myhunter.cuny.edu
#Date: October 31, 2022
#This program prints perfect number


def isPerfect(num):
    if num <=0:
        return False
    total=0
    for i in range(1,num//2+1):
        if num%i==0:
            total+=i
    if total==num:
        return True
    else:
        return False

def main():
    num=int (input("Enter a perfect integer: "))
    while not(isPerfect(num)):
        num = int(input(f"{num} is not a perfect number. Re-enter "))
    print(f"Congratulations! {num} is a perfect number.")
main()


    

