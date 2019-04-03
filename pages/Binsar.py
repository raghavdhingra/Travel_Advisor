import folium
import os

m = folium.Map(location=[27.9305, 88.7346], zoom_start=10)

tooltip = 'Click For More Info'

vis = os.path.join('data', 'vis.json')

overlay = os.path.join('data', 'overlay.json')

# BINSAR
# Create markers(tourist spots)
folium.Marker([27.9305, 88.7346],
              popup=folium.Popup('<a href="map.html" target="blank"><strong>Zero Point</strong></a>'),
              icon=folium.Icon(icon='star'),
              tooltip=tooltip).add_to(m),
folium.Marker([27.9500, 88.7428],
              popup=folium.Popup('<a href="map.html" target="blank"><strong>Pariyadeva Pashan</strong></a>'),
              icon=folium.Icon(icon='star'),
              tooltip=tooltip).add_to(m),
folium.Marker([29.6968, 79.7534],
              popup=folium.Popup('<a href="map.html" target="blank"><strong>Marry Budden Estate</strong></a>'),
              icon=folium.Icon(icon='star'),
              tooltip=tooltip).add_to(m),


# Create marker(hotels)
folium.Marker([29.7049, 79.7490],
              popup=folium.Popup('<a href="map.html" target="blank"><strong>Binsar Forest Retreat</strong></a>'),
              icon=folium.Icon(color='green', icon='home'),
              tooltip=tooltip).add_to(m),
folium.Marker([29.6736, 79.7878],
              popup=folium.Popup('<a href="map.html" target="blank"><strong>Binsar Eco Camp</strong></a>'),
              icon=folium.Icon(color='green', icon='home'),
              tooltip=tooltip).add_to(m),
folium.Marker([29.6989, 79.7028],
              popup=folium.Popup('<a href="map.html" target="blank"><strong>Club Mahindra Binsar Valley</strong></a>'),
              icon=folium.Icon(color='green', icon='home'),
              tooltip=tooltip).add_to(m),


# Generate map
m.save('Binsar.html')

