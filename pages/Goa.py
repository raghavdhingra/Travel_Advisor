import folium
import os

m = folium.Map(location=[15.5006, 73.8313], zoom_start=12)

tooltip = 'Click For More Info'

vis = os.path.join('data', 'vis.json')

overlay = os.path.join('data', 'overlay.json')

# GOA
# Create markers(tourist spots)
folium.Marker([15.5494, 73.7535],
              popup=folium.Popup('<a href="Calangute/html/index.html" target="blank"><strong>Calangute Beach</strong></a>'),
              icon=folium.Icon(icon='star'),
              tooltip=tooltip).add_to(m),
folium.Marker([15.4926, 73.7737],
              popup=folium.Popup('<a href="https://www.travelogyindia.com/goa/fort-aguda.html" target="blank"><strong>Fort Aguada</strong></a>'),
              icon=folium.Icon(icon='star'),
              tooltip=tooltip).add_to(m),
folium.Marker([15.5006, 73.8313],
              popup=folium.Popup('<a href="https://india.gobananas.com/activities/goa/night/casino-deltin-royal" target="blank"><strong>Deltin Royale Casino</strong></a>'),
              icon=folium.Icon(icon='star'),
              tooltip=tooltip).add_to(m),


# Create marker(hotels)
folium.Marker([15.5444, 73.9248],
              popup=folium.Popup('<a href="Taj/index.html" target="blank"><strong>Taj Exotica and Spa</strong></a>'),
              icon=folium.Icon(color='green', icon='home'),
              tooltip=tooltip).add_to(m),
folium.Marker([15.5061, 73.7699],
              popup=folium.Popup('<a href="map.html" target="blank"><strong>Santana Beach Resort</strong></a>'),
              icon=folium.Icon(color='green', icon='home'),
              tooltip=tooltip).add_to(m),
folium.Marker([15.5738, 73.7599],
              popup=folium.Popup('<a href="map.html" target="blank"><strong>Park Regis</strong></a>'),
              icon=folium.Icon(color='green', icon='home'),
              tooltip=tooltip).add_to(m),

# Foods
folium.Marker([15.5346, 73.7580],
              popup=folium.Popup('<a href="https://lbb.in/goa/rustic-simplicity-pousada-by-the-beach-goa/" target="blank"><strong>Pousada By The Beach</strong></a>'),
              icon=folium.Icon(color='red', icon='cutlery'),
              tooltip=tooltip).add_to(m),
folium.Marker([15.4984, 73.8266],
              popup=folium.Popup('<a href="goa_cuisine/index.html" target="blank"><strong>Ritz Classic Restaurant and Bar</strong></a>'),
              icon=folium.Icon(color='red', icon='cutlery'),
              tooltip=tooltip).add_to(m),
folium.Marker([15.5389, 73.8184],
              popup=folium.Popup('<a href="http://www.copperleafgoa.com/" target="blank"><strong>Copperleaf</strong></a>'),
              icon=folium.Icon(color='red', icon='cutlery'),
              tooltip=tooltip).add_to(m),



# Generate map
m.save('Goa.html')

