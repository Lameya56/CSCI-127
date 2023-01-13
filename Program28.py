#Name: Lameya Mostafa
#Email: Lameya.mostafa18@myhunter.cuny.edu
#Date: October 16, 2022
#This program prints lead affected children

import pandas as pd

lead = pd.read_csv("children_lead.csv")
choice = input("Enter a choice:\na. group by borough \nb. group by year \n")

if choice == "a":
    print("average number of affected children by borough")
    print(lead.groupby("borough")["affected_children"].mean())
    select= input("Enter a borough: ")
    chosen= lead.groupby("borough").get_group(select)
    print("average number of affected children of "+ select+ " is  " + str(chosen["affected_children"].mean()))
    print("min number of affected children of "+ select + " is  "+ str(chosen["affected_children"].min()))
    print("max number of affected children of "+ select + " is  "+ str(chosen["affected_children"].max()))
elif choice=="b":
    print("average number of affected children by year")
    print(lead.groupby("year")["affected_children"].mean())
    number= int(input("Enter a year (2005 - 2016): "))
    children = lead.groupby("year").get_group(number)
    print("average number of affected children in "+ str(number)+" is "+str(children["affected_children"].mean()))
    print("min number of affected children in "+str(number)+" is "+str(children["affected_children"].min()))
    print("max number of affected children in "+ str(number)+" is " + str(children["affected_children"].max()))
else: 
    print("wrong choice")
