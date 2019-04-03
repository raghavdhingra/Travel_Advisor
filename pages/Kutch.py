import folium
import os

m = folium.Map(location=[23.2546, 69.6685], zoom_start=10)

tooltip = 'Click For More Info'

vis = os.path.join('data', 'vis.json')

overlay = os.path.join('data', 'overlay.json')

# KUTCH
# Create markers(tourist spots)
folium.Marker([23.2546, 69.6685],
              popup=folium.Popup('<a href="map.html" target="blank"><strong>Prag Mahal</strong></a>'),
              icon=folium.Icon(icon='star'),
              tooltip=tooltip).add_to(m),
folium.Marker([23.9345, 69.8145],
              popup=folium.Popup('<a href="map.html" target="blank"><strong>Kalo Dungar</strong></a>'),
              icon=folium.Icon(icon='star'),
              tooltip=tooltip).add_to(m),
folium.Marker([23.2487, 69.6663],
              popup=folium.Popup('<a href="map.html" target="blank"><strong>Kutch Museum</strong></a>'),
              icon=folium.Icon(icon='star'),
              tooltip=tooltip).add_to(m),


# Create marker(hotels)
folium.Marker([23.2349, 69.6457],
              popup=folium.Popup('<a href="map.html" target="blank"><strong>Regenta Resort Bhuj</strong></a>'),
              icon=folium.Icon(color='green', icon='home'),
              tooltip=tooltip).add_to(m),
folium.Marker([23.0634, 70.1326],
              popup=folium.Popup('<a href="map.html" target="blank"><strong>Ambar Sarovar Portico</strong></a>'),
              icon=folium.Icon(color='green', icon='home'),
              tooltip=tooltip).add_to(m),
folium.Marker([23.2418, 69.6399],
              popup=folium.Popup('<a href="map.html" target="blank"><strong>Divya Jot Residency</strong></a>'),
              icon=folium.Icon(color='green', icon='home'),
              tooltip=tooltip).add_to(m),


# Generate map
m.save('Kutch.html')

