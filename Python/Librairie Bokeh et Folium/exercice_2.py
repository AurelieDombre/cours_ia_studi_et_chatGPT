import folium

# 1. Définition des coordonnées (trouvées via géocodage)
entrepots = [ {"nom": "Entrepôt Paris", "coordonnees": [48.8566, 2.3522], "couleur": "green"},
              {"nom": "Entrepôt Bordeaux", "coordonnees": [44.8378, -0.5792], "couleur": "orange"},
              {"nom": "Entrepôt Toulouse", "coordonnees": [43.6047, 1.4442], "couleur": "lightgray"},
              {"nom": "Entrepôt Marseille", "coordonnees": [43.2965, 5.3698], "couleur": "darkblue"}
              ]
# 2. Initialisation de la carte
ma_carte = folium.Map(location=[44.4, 2.3], zoom_start=9)

# 3. LA BOUCLE : On parcourt chaque dictionnaire de la liste
for entrepot in entrepots:
    folium.Marker(
        location=entrepot["coordonnees"],
        popup=f"<b>{entrepot['nom']}", # HTML possible dans le popup
        tooltip=entrepot["nom"],
        icon=folium.Icon(color=entrepot["couleur"], icon="info-sign")
    ).add_to(ma_carte)

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


# 4. Sauvegarde
ma_carte.save("carte_entrepots.html")