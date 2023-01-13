#Name: Lameya Mostafa
#Email: Lameya.mostafa18@myhunter.cuny.edu
#Date: October 20, 2022
#This program maps NYC Central park

import folium

mapNYC = folium.Map(location=[40.75, -74.125], zoom_start=10)

folium.Marker(location = [40.7812, -73.9665], popup = "Central Park").add_to(mapNYC)
mapNYC.save(outfile= "nyc_Central_Park.html")

