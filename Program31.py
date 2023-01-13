#Name: Lameya Mostafa
#Email: Lameya.mostafa18@myhunter.cuny.edu
#Date: October 17, 2022
#This program prints internet users in population percentage
import pandas as pd
import matplotlib.pyplot as plt

in_file= pd.read_csv("country_internet.csv")
out_file = input("Enter name of output file:  ")
in_file["Percentage"]= in_file["Internet users"]/in_file["Population"]*100
in_file.plot(x="Country", y= "Percentage" )
plt.savefig(out_file)
#plt.show()