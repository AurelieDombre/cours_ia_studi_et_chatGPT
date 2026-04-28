import folium

# 1. Définition des coordonnées (trouvées via géocodage)
# Adresse 1 : 24 route de rodez, 12440 La Salvetat-Peyralès
loc_salvetat = [44.2205, 2.2032]

# Adresse 2 : 6 place barthal, 46100 Figeac
loc_figeac = [44.6074, 2.0341]

# 2. Création de la carte
# On centre la carte entre les deux points (environ)
ma_carte = folium.Map(location=[44.4, 2.1], zoom_start=10)

# 3. Ajout des marqueurs
folium.Marker(
    location=loc_salvetat,
    popup="La Salvetat-Peyralès",
    tooltip="24 route de Rodez",
    icon=folium.Icon(color="blue", icon="home")
).add_to(ma_carte)

folium.Marker(
    location=loc_figeac,
    popup="Figeac",
    tooltip="6 place Barthal",
    icon=folium.Icon(color="green", icon="info-sign")
).add_to(ma_carte)

# Ajouter un trait entre 2 points
folium.PolyLine(locations=[loc_salvetat, loc_figeac]).add_to(ma_carte)

#Ajouter les couches de tuiles
folium.TileLayer(  tiles='https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
name='ESRI World Imagery',
attr='Tiles © Esri'
).add_to(ma_carte)
folium.TileLayer( tiles='https://server.arcgisonline.com/ArcGIS/rest/services/World_Topo_Map/MapServer/tile/{z}/{y}/{x}',
name='ESRI World Topo Map',
attr='Tiles © Esri'
).add_to(ma_carte)

#Ajouter le contrôle de couches
folium.LayerControl().add_to(ma_carte)

# 4. Sauvegarde et affichage
ma_carte.save("ma_carte_aveyron_lot.html")
print("La carte a été générée dans le fichier 'ma_carte_aveyron_lot.html'")