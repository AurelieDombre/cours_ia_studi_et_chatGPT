from classes.model.bibliotheque import Bibliotheque
from classes.model.livre import Livre

mon_livre = Livre("Python", "Lilie", 10 )
mon_livre.afficher_info()

livre_1 = Livre("Python volume 2", "Livre", 10 )

ma_bibliotheque = Bibliotheque()
ma_bibliotheque.ajouter_livre(livre_1)

ma_bibliotheque.liste_livres()