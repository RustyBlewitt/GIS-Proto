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

mymap = folium.Map(location=[34.7, -116], zoom_start = 5)

# Child object, layer: locations of volcanoes as points
volcano_points = folium.FeatureGroup(name="Volcanoes")

# add points to volcano layer
for lat, lon, name, elev in zip(df['LAT'], df['LON'], df['NAME'], df['ELEV']):
    popup = "(%f, %f) %s %sm" %(lat, lon, name, elev)
    volcano_points.add_child(folium.CircleMarker(location=[lat, lon], popup=popup, radius = 5,
    color = color_picker(elev), fill_color = "white", fill_opacity = 0.8))

# Child object, layer: countries as polygons, color coded by population
country_polygons = folium.FeatureGroup(name="Countries")

# add polygons to country layer
country_polygons.add_child(folium.GeoJson(data=open('countries.json', 'r', encoding='utf-8-sig').read(), 
style_function=lambda x:{'fillColor':'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 < x['properties']['POP2005'] <  20000000 else 'red'}))


mymap.add_child(volcano_points)
mymap.add_child(country_polygons)
mymap.add_child(folium.LayerControl())

mymap.save('map.html')