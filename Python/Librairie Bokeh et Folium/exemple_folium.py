import folium

# Créer une carte centrée sur Paris, France
mymap = folium.Map(location=[48.8566, 2.3522], zoom_start=13)

# Ajouter un marqueur pour Paris
folium.Marker([48.8566, 2.3522], popup="Paris").add_to(mymap)

# Enregistrer la carte dans un fichier HTML
mymap.save("mymap.html")