#Name: Lameya Mostafa
#Email: Lameya.mostafa18@myhunter.cuny.edu
#Date: October 20, 2022
#This program maps NYC Central park

import folium
import pandas as pd
nyc_hospitals= pd.read_csv("nyc_hospitals.csv")
mapHosp= folium.Map(zoom_start=10)
output= input("Enter output file:  ")
for index,row in nyc_hospitals.iterrows():
    lat = row["Latitude"]
    lon = row["Longitude"]
    name = row["Facility Name"]
    newMarker = folium.Marker([lat, lon], popup=name)
    newMarker.add_to(mapHosp)



mapHosp.save(outfile=output)