import folium
import os

m = folium.Map(location=[31.0979, 77.2678], zoom_start=11)

tooltip = 'Click For More Info'

vis = os.path.join('data', 'vis.json')

overlay = os.path.join('data', 'overlay.json')

# SHIMLA
# Create markers(tourist spots)
folium.Marker([31.0979, 77.2678],
              popup=folium.Popup('<a href="map.html" target="blank"><strong>Kufri</strong></a>'),
              icon=folium.Icon(icon='star'),
              tooltip=tooltip).add_to(m),
folium.Marker([31.2249, 77.3569],
              popup=folium.Popup('<a href="map.html" target="blank"><strong>Chadwick Falls</strong></a>'),
              icon=folium.Icon(icon='star'),
              tooltip=tooltip).add_to(m),
folium.Marker([31.1196, 77.1389],
              popup=folium.Popup('<a href="map.html" target="blank"><strong>Mall Road</strong></a>'),
              icon=folium.Icon(icon='star'),
              tooltip=tooltip).add_to(m),


# Create marker(hotels)
folium.Marker([31.1115, 77.1774],
              popup=folium.Popup('<a href="map.html" target="blank"><strong>Raddison Jass</strong></a>'),
              icon=folium.Icon(color='green', icon='home'),
              tooltip=tooltip).add_to(m),
folium.Marker([31.1141, 77.1303],
              popup=folium.Popup('<a href="map.html" target="blank"><strong>Shimla Nature Villa</strong></a>'),
              icon=folium.Icon(color='green', icon='home'),
              tooltip=tooltip).add_to(m),
folium.Marker([31.1060, 77.1326],
              popup=folium.Popup('<a href="map.html" target="blank"><strong>Evoke Shimla Heaven Resort </strong></a>'),
              icon=folium.Icon(color='green', icon='home'),
              tooltip=tooltip).add_to(m),


# Generate map
m.save('Shimla.html')

