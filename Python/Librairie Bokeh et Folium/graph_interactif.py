import numpy as np
from bokeh.io import curdoc
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource, Slider # Import Slider ajouté
from bokeh.layouts import column

# 1. Préparation des données plus précises
x = np.linspace(0, 10, 500) # De 0 à 10 avec 500 points pour la fluidité
y = np.sin(x)
source = ColumnDataSource(data={'x': x, 'y': y})

# 2. Création de la figure
# Correction de x_range pour voir toute la courbe
plot = figure(title="Exemple de vague dynamique",
              x_range=[0, 10],
              y_range=[-1.5, 1.5])

plot.line(x='x', y='y', source=source, line_width=3, color="navy")

# 3. Création du slider
slider = Slider(start=0.1, end=10, value=1, step=0.1, title="Fréquence")

# 4. Fonction de mise à jour (Callback)
def update_data(attr, old, new):
    f = slider.value # On récupère la valeur actuelle du curseur
    new_y = np.sin(f * x) # On recalcule les coordonnées Y
    source.data = {'x': x, 'y': new_y} # On remplace les données de la source

# 5. Liaison : dès que la 'value' du slider change, on appelle update_data
slider.on_change('value', update_data)

# 6. Mise en page et ajout au document
layout = column(slider, plot)
curdoc().add_root(layout)
curdoc().title = "Onde Interactive"