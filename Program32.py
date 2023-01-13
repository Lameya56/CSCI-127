#Name: Lameya Mostafa
#Email: Lameya.mostafa18@myhunter.cuny.edu
#Date: October 17, 2022
#This program prints average number of plans by region

import pandas as pd
import matplotlib.pyplot as plt

internet= pd.read_csv("country_internet.csv")
print(internet.groupby("Continental region")["NO. OF Internet Plans"].mean())
print("possible regions are")
print(internet.groupby("Continental region").groups.keys())

region = input("choose a region: ")
print("In region "+ region)
specific_region= (internet.groupby("Continental region")).get_group(region)
print("number of countries:  "+ str(specific_region["Country"].nunique()))
print("maximum number of internet plans:  "+ str(specific_region["NO. OF Internet Plans"].max()))
print("minimum number of internet plans:  "+ str(specific_region["NO. OF Internet Plans"].min()))

out_file= input("Please enter output file name: ")
internet.groupby("Continental region").get_group(region).plot.bar("Country","NO. OF Internet Plans")
    #the first parameter of bar method is the column name representing country, the second parameter is the number of internet plans
plt.gcf().subplots_adjust(bottom=0.25)
    #so that the country name is displayed in full
plt.xlabel("Country in "+ region)
    #The parameter in xlabel should be "Country in ...", where ... is the name of chosen region. The region name should be exactly the same as the corresponding region the csv file.
plt.ylabel("NO. OF Internet Plans")
plt.savefig(out_file)
#plt.show()

