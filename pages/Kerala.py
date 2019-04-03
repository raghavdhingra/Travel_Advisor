import folium
import os

m = folium.Map(location=[9.4927, 76.4286], zoom_start=8)

tooltip = 'Click For More Info'

vis = os.path.join('data', 'vis.json')

overlay = os.path.join('data', 'overlay.json')

# KERALA
# Create markers(tourist spots)
folium.Marker([9.4927, 76.4286],
              popup=folium.Popup('<a href="map.html" target="blank"><strong>Alappuzha Beach</strong></a>'),
              icon=folium.Icon(icon='star'),
              tooltip=tooltip).add_to(m),
folium.Marker([9.6247, 76.4286],
              popup=folium.Popup('<a href="map.html" target="blank"><strong>Kuamarakom Bird Sanctuary </strong></a>'),
              icon=folium.Icon(icon='star'),
              tooltip=tooltip).add_to(m),
folium.Marker([9.8945, 76.5536],
              popup=folium.Popup('<a href="map.html" target="blank"><strong>Ekkdal Caves</strong></a>'),
              icon=folium.Icon(icon='star'),
              tooltip=tooltip).add_to(m),


# Create marker(hotels)
folium.Marker([10.5940, 76.0369],
              popup=folium.Popup('<a href="map.html" target="blank"><strong>Srivar Hotel</strong></a>'),
              icon=folium.Icon(color='green', icon='home'),
              tooltip=tooltip).add_to(m),
folium.Marker([10.5223, 76.2131],
              popup=folium.Popup('<a href="map.html" target="blank"><strong>Hotel Pooram International</strong></a>'),
              icon=folium.Icon(color='green', icon='home'),
              tooltip=tooltip).add_to(m),
folium.Marker([10.0398, 77.1670],
              popup=folium.Popup('<a href="map.html" target="blank"><strong>Streling Munnar- Resorts and Spa</strong></a>'),
              icon=folium.Icon(color='green', icon='home'),
              tooltip=tooltip).add_to(m),


# Generate map
m.save('Kerala.html')

