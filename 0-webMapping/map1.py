import folium
import pandas
import json


# Datas needed to manipulate the map
volcanoes_data = pandas.read_csv('./data/Volcanoes.txt')
# folium.GeoJson expects json in utf-8-sig encoding
population_data = json.load(open('./data/world.json', encoding='utf-8-sig'))


# Get the needed data to place markers in map
lat = list(volcanoes_data['LAT'])
lon = list(volcanoes_data['LON'])
elev = list(volcanoes_data['ELEV'])
name = list(volcanoes_data['NAME'])


# Markup to show on click of marker
html = """<h4>Volcano information:</h4>
<a href="https://www.google.com/search?q={name}" target="_blank">{name}</a><br />
Height: {elev} m
"""


# To get color of marker based on elevation of volcanoes
def color_producer(elevation):
    if isinstance(elevation, (float, int)):
        if elevation < 1000:
            return 'green'
        elif 1000 <= elevation < 3000:
            return 'orange'
        else:
            return 'red'
    else:
        return 'green'


# Generate the empty map object
map = folium.Map(location=[38.58, -99.09],
                 zoom_start=6, tiles="Stamen Terrain")


# Create a seperate feature group that we want to control it in layerControl
fgv = folium.FeatureGroup(name="Volcanoes")
fgp = folium.FeatureGroup(name="Population")


# plot the country's borders and color it based on its population
fgp.add_child(folium.GeoJson(data=population_data,
                             style_function=lambda x: {"fillColor": "green" if x['properties']['POP2005'] < 10000000 else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))


# Plot the markers on location of volcaneos
for lt, ln, el, name in zip(lat, lon, elev, name):
    iframe = folium.IFrame(html=html.format(
        elev=el, name=name), width=200, height=100)

    fgv.add_child(folium.CircleMarker(location=[lt, ln], popup=folium.Popup(
        iframe), tooltip="Click me", radius=8, fill_color=color_producer(el),  color="grey", fill_opacity=0.7))

    # fg.add_child(folium.Marker(location=[
    #     lt, ln], popup=folium.Popup(iframe), tooltip="Click me", icon=folium.Icon(color=color_producer(el))))


# append the Feature groups to map
map.add_child(fgv)
map.add_child(fgp)


# apply the LayerControl only after the featrue group added to map
map.add_child(folium.LayerControl())


# save the map as html file in a given path, so we can view it in browser
map.save("Map1.html")
