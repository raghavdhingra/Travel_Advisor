import folium
import os

m = folium.Map(location=[12.4571, 75.7164], zoom_start=10)

tooltip = 'Click For More Info'

vis = os.path.join('data', 'vis.json')

overlay = os.path.join('data', 'overlay.json')

# COORG
# Create markers(tourist spots)
folium.Marker([12.4571, 75.7164],
              popup=folium.Popup('<a href="map.html" target="blank"><strong>Abbey Falls</strong></a>'),
              icon=folium.Icon(icon='star'),
              tooltip=tooltip).add_to(m),
folium.Marker([12.2348, 75.6407],
              popup=folium.Popup('<a href="map.html" target="blank"><strong>Nalknad Palace</strong></a>'),
              icon=folium.Icon(icon='star'),
              tooltip=tooltip).add_to(m),
folium.Marker([12.3465, 75.8417],
              popup=folium.Popup('<a href="map.html" target="blank"><strong>Barapole River</strong></a>'),
              icon=folium.Icon(icon='star'),
              tooltip=tooltip).add_to(m),


# Create marker(hotels)
folium.Marker([12.3293, 75.8626],
              popup=folium.Popup('<a href="map.html" target="blank"><strong>Zoostel Coorg</strong></a>'),
              icon=folium.Icon(color='green', icon='home'),
              tooltip=tooltip).add_to(m),
folium.Marker([12.4310, 75.7536],
              popup=folium.Popup('<a href="map.html" target="blank"><strong>Treebo Vrindavan Coorg</strong></a>'),
              icon=folium.Icon(color='green', icon='home'),
              tooltip=tooltip).add_to(m),
folium.Marker([12.5064, 75.9484],
              popup=folium.Popup('<a href="map.html" target="blank"><strong>Parampara Resort and Spa</strong></a>'),
              icon=folium.Icon(color='green', icon='home'),
              tooltip=tooltip).add_to(m),


# Generate map
m.save('Coorg.html')

