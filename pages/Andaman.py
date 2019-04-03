import folium
import os

m = folium.Map(location=[11.4521, 92.7056], zoom_start=9)

tooltip = 'Click For More Info'

vis = os.path.join('data', 'vis.json')

overlay = os.path.join('data', 'overlay.json')

# ANDAMAN
# Create markers(tourist spots)
folium.Marker([11.4521, 92.7056],
              popup=folium.Popup('<a href="map.html" target="blank"><strong>Cellular Jail National Memorial</strong></a>'),
              icon=folium.Icon(icon='star'),
              tooltip=tooltip).add_to(m),
folium.Marker([11.9845, 92.9508],
              popup=folium.Popup('<a href="map.html" target="blank"><strong>Radhanagar Beach</strong></a>'),
              icon=folium.Icon(icon='star'),
              tooltip=tooltip).add_to(m),
folium.Marker([11.5060, 92.7015],
              popup=folium.Popup('<a href="map.html" target="blank"><strong>Chidiya Tapu</strong></a>'),
              icon=folium.Icon(icon='star'),
              tooltip=tooltip).add_to(m),


# Create marker(hotels)
folium.Marker([11.8838, 93.0560],
              popup=folium.Popup('<a href="map.html" target="blank"><strong>Taj Exotica Resort And Spa</strong></a>'),
              icon=folium.Icon(color='green', icon='home'),
              tooltip=tooltip).add_to(m),
folium.Marker([12.0283, 93.0017],
              popup=folium.Popup('<a href="map.html" target="blank"><strong>Symphony Palm Beach Resort</strong></a>'),
              icon=folium.Icon(color='green', icon='home'),
              tooltip=tooltip).add_to(m),
folium.Marker([12.3162, 92.8428],
              popup=folium.Popup('<a href="map.html" target="blank"><strong>Summer Sands Beach Resort</strong></a>'),
              icon=folium.Icon(color='green', icon='home'),
              tooltip=tooltip).add_to(m),

#Foods
folium.Marker([12.0213, 93.0063],
              popup=folium.Popup('<a href="map.html" target="blank"><strong>Fat Martin</strong></a>'),
              icon=folium.Icon(color='red', icon='cutlery'),
              tooltip=tooltip).add_to(m),
folium.Marker([12.0357, 92.9897],
              popup=folium.Popup('<a href="map.html" target="blank"><strong>Beachside Cafe</strong></a>'),
              icon=folium.Icon(color='red', icon='cutlery'),
              tooltip=tooltip).add_to(m),
folium.Marker([12.0236, 93.0044],
              popup=folium.Popup('<a href="map.html" target="blank"><strong>Anju Coco Resto</strong></a>'),
              icon=folium.Icon(color='red', icon='cutlery'),
              tooltip=tooltip).add_to(m),




# Generate map
m.save('Andaman.html')

