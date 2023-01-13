#Name: Lameya Mostafa
#Email: Lameya.mostafa18@myhunter.cuny.edu
#Date: October 16, 2022
#This program prints words ending with a or b

import matplotlib.pyplot as plt
import pandas as pd

covid= pd.read_csv(input("Enter a csv file: "))
borough= input("Enter borough (Bronx, Brooklyn, Queens, Manhattan, Staten Island): ")
output = input("Enter output name: ")

minimum= covid[borough].min()
print ("Min: "+ str(minimum))
Maximum= covid[borough].max()
print("Max: "+ str(Maximum))
mean= round(covid[borough].mean(),3)
print("Mean: "+ str(mean))
median= round(covid[borough].median(),3)
print("Median: "+ str(median))
st_deviation= round(covid[borough].std(),3)
print("Standard Deviation: "+ str(st_deviation))

covid["Fraction"] = covid[borough]/covid["case_count"]
covid.plot(x= "date_of_interest", y= covid["Fraction"])



#fig = covid.gfc()
#fig.getfig(output)

plt.savefig(output)
