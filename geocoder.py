import folium
import pandas as pd

def color_picker(elev):
    if elev < 1000:
        return "green"
    elif 1000 <= elev <= 3000:
        return "orange"
    else:
        return "red"

df = pd.read_csv("Volcanoes.txt")
print(df.head(90))

mymap = folium.Map(location=[34.7, -116], zoom_start = 8)
fg = folium.FeatureGroup(name="My FG")

for lat, lon, name, elev in zip(df['LAT'], df['LON'], df['NAME'], df['ELEV']):
    popup = "(%f, %f) %s %sm" %(lat, lon, name, elev)
    fg.add_child(folium.CircleMarker(location=[lat, lon], popup=popup, radius = 5,
    color = color_picker(elev), fill_color = "white", fill_opacity = 0.8))

mymap.add_child(fg)
mymap.save('map.html')