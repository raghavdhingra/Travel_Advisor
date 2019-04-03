import folium
import os

m = folium.Map(location=[33.4562, 78.0325], zoom_start=7)

tooltip = 'Click For More Info'

vis = os.path.join('data', 'vis.json')

overlay = os.path.join('data', 'overlay.json')

# Leh Ladakh
# Create markers(tourist spots)
folium.Marker([33.4562, 78.0325],
              popup=folium.Popup('<a href="http://vargiskhan.com/log/zanskar-valley-itinerary-sample-travel-plan/" target="blank"><strong>Zanskar Valley</strong></a>'),
              icon=folium.Icon(icon='star'),
              tooltip=tooltip).add_to(m),
folium.Marker([33.7595, 78.6675],
              popup=folium.Popup('<a href="https://www.lehladakhindia.com/pangong-tso-lake/" target="blank"><strong>Pangong Tso Lake</strong></a>'),
              icon=folium.Icon(icon='star'),
              tooltip=tooltip).add_to(m),
folium.Marker([32.9856, 78.9654],
              popup=folium.Popup('<a href="https://www.tourmyindia.com/states/jammu-kashmir/khardung-la-pass.html" target="blank"><strong>Khardung-La Pass</strong></a>'),
              icon=folium.Icon(icon='star'),
              tooltip=tooltip).add_to(m),


# Create marker(hotels)
folium.Marker([34.1566, 77.5805],
              popup=folium.Popup('<a href="map.html" target="blank"><strong>The Grand Dragon</strong></a>'),
              icon=folium.Icon(color='green', icon='home'),
              tooltip=tooltip).add_to(m),
folium.Marker([34.1587, 77.5746],
              popup=folium.Popup('<a href="map.html" target="blank"><strong>The Zen Ladakh Resort</strong></a>'),
              icon=folium.Icon(color='green', icon='home'),
              tooltip=tooltip).add_to(m),
folium.Marker([34.1616, 77.5834],
              popup=folium.Popup('<a href="map.html" target="blank"><strong>Hotel Singge Palace</strong></a>'),
              icon=folium.Icon(color='green', icon='home'),
              tooltip=tooltip).add_to(m),

# Foods
folium.Marker([34.1638, 77.5812],
              popup=folium.Popup('<a href="https://www.lonelyplanet.com/india/leh/restaurants/tibetan-kitchen/a/poi-eat/1545501/356310" target="blank"><strong>Tibetan Kitchen</strong></a>'),
              icon=folium.Icon(color='red', icon='cutlery'),
              tooltip=tooltip).add_to(m),
folium.Marker([34.1526, 77.5771],
              popup=folium.Popup('<a href="https://foursquare.com/v/yum-yum--real-coffee--french-bakery/560c95c5498ebf43db239565" target="blank"><strong>Yum Yum Food Cafe</strong></a>'),
              icon=folium.Icon(color='red', icon='cutlery'),
              tooltip=tooltip).add_to(m),
folium.Marker([34.1643, 77.5843],
              popup=folium.Popup('<a href="" target="blank"><strong>Appletree Restaurant And German Bakery</strong></a>'),
              icon=folium.Icon(color='red', icon='cutlery'),
              tooltip=tooltip).add_to(m),



# Generate map
m.save('Leh_ladakh.html')

