# Importation des modules nécessaires
from bokeh.layouts import column
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure, output_file, show

mois = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
utilisateurs = [1200, 1500, 1700, 1800, 2200, 2500, 2700, 3000, 3200, 3500, 3700, 4000]

# Créer une figure
p = figure(title="Croissance des utilisateurs mensuels", x_axis_label='Mois', y_axis_label='Nombre d\'utilisateurs', x_range=mois)

# Ajouter une ligne
p.line(mois, utilisateurs, legend_label="Utilisateurs", line_width=2)

# Ajouter des cercles aux points de données
p.circle(mois, utilisateurs, size=10, color="navy", alpha=0.5)

# Définir le fichier de sortie
output_file("croissance_utilisateurs.html")

# Afficher le graphique
show(p)