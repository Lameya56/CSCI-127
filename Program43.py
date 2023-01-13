#Name: Lameya Mostafa
#Email: Lameya.mostafa18@myhunter.cuny.edu
#Date: October 21, 2022
#This program maps NYC afterschool program

import folium
import pandas as pd

school= pd.read_csv("after_school.csv")
choice= input("Enter 1 for Borough/Community,\n2 for Grade Level / Age Group\nYour choice: ")

if choice=="1":
    print(school.groupby("Borough/Community").groups.keys())
    chosenBorough= input("Enter Borough/Community name: ")
    borough_info= school.groupby("Borough/Community").get_group(chosenBorough)
    mapBorough= folium.Map()
    for index,row in borough_info.iterrows():
        lat = row["Latitude"]
        lon = row["Longitude"]
        newMarker = folium.Marker([lat, lon], popup=["Name"])
        newMarker.add_to(mapBorough)
    output = chosenBorough.lower().replace(' ','_').replace('/','_')+"_after_school"
    mapBorough.save(output+".html")
if choice=="2":
    print(school.groupby("Grade Level / Age Group").groups.keys())
    chosen_grade_age= input("Enter Grade Level / Age Group name: ")
    mapgrade=folium.Map()
    location_grade= school.groupby("Grade Level / Age Group").get_group(chosen_grade_age)
    for index,row in location_grade.iterrows():
        lat = row["Latitude"]
        lon = row["Longitude"]
        newMarker = folium.Marker([lat, lon], popup=["Name"])
        newMarker.add_to(mapgrade)
    output=chosen_grade_age.lower().replace(" ","_").replace("/","_")+"_after_school"
    mapgrade.save(output+".html")
    
