import folium
import os

m = folium.Map(location=[34.1229, 74.8630], zoom_start=12)

tooltip = 'Click For More Info'

vis = os.path.join('data', 'vis.json')

overlay = os.path.join('data', 'overlay.json')

# SRINAGAR
# Create markers(tourist spots)
folium.Marker([34.1229, 74.8630],
              popup=folium.Popup('<a href="https://www.beautifulworld.com/asia/india/dal-lake/" target="blank"><strong>Dal Lake</strong></a>'),
              icon=folium.Icon(icon='star'),
              tooltip=tooltip).add_to(m),
folium.Marker([34.1229, 74.8794],
              popup=folium.Popup('<a href="https://www.tourmyindia.com/states/jammu-kashmir/nishant-garden.html" target="blank"><strong>Nishat Bagh</strong></a>'),
              icon=folium.Icon(icon='star'),
              tooltip=tooltip).add_to(m),
folium.Marker([34.1485, 74.8696],
              popup=folium.Popup('<a href="https://www.tourmyindia.com/states/jammu-kashmir/shalimar-garden.html" target="blank"><strong>Shalimar Bagh</strong></a>'),
              icon=folium.Icon(icon='star'),
              tooltip=tooltip).add_to(m),


# Create marker(hotels)
folium.Marker([34.1026, 74.8814],
              popup=folium.Popup('<a href="map.html" target="blank"><strong>Vivanta by Taj</strong></a>'),
              icon=folium.Icon(color='green', icon='home'),
              tooltip=tooltip).add_to(m),
folium.Marker([34.1740, 74.8261],
              popup=folium.Popup('<a href="map.html" target="blank"><strong>The Orchard Retreat & Spa </strong></a>'),
              icon=folium.Icon(color='green', icon='home'),
              tooltip=tooltip).add_to(m),
folium.Marker([34.1160, 74.8293],
              popup=folium.Popup('<a href="map.html" target="blank"><strong>Peacock House Boat</strong></a>'),
              icon=folium.Icon(color='green', icon='home'),
              tooltip=tooltip).add_to(m),

#Foods
folium.Marker([34.0724, 74.8190],
              popup=folium.Popup('<a href="map.html" target="blank"><strong>Ahdoos Hotel</strong></a>'),
              icon=folium.Icon(color='red', icon='cutlery'),
              tooltip=tooltip).add_to(m),
folium.Marker([34.0849, 74.7978],
              popup=folium.Popup('<a href="http://www.lacimacafe.com/" target="blank"><strong>Lacima Cafe And Pizzeria</strong></a>'),
              icon=folium.Icon(color='red', icon='cutlery'),
              tooltip=tooltip).add_to(m),
folium.Marker([34.0819, 74.8320],
              popup=folium.Popup('<a href="http://www.steamrestaurantilm.com/" target="blank"><strong>Stream Restaurant</strong></a>'),
              icon=folium.Icon(color='red', icon='cutlery'),
              tooltip=tooltip).add_to(m),


# Generate map
m.save('Srinagar.html')

