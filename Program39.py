#Name: Lameya Mostafa
#Email: Lameya.mostafa18@myhunter.cuny.edu
#Date: October 18, 2022
#This program prints movie sites
import pandas as pd
movies= pd.read_csv("movie_locations.csv")
popular=int(input("order of most popular neighborhoods in movies: "))
print(movies["Neighborhood"].value_counts().head(popular))
film_makers= int(input("order of directors/filmmakers making most movies in NYC: "))
print(movies["Director/Filmmaker Name"].value_counts().head(film_makers))