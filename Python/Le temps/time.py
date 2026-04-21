
# Dans cet exercice, nous allons d’abord définir deux fonctions :
#
# trace(), qui permet de « tracer » ou d’enregistrer une ligne de log. Cette fonction doit d’abord récupérer le temps exact à laquelle elle est appelée, pour ensuite imprimer le message souhaité précédé du temps,
#
# get_time() permet tout simplement de renvoyer le temps courant
#
# Ensuite, nous définissons un programme qui réalise 10 boucles. Pour simuler un process, nous avons utilisé l’instruction time.sleep(1), qui bloquera le programme durant 1 seconde à chaque appel.

from datetime import datetime
import time

def trace(my_log_line):
    timestamp = get_time()
    print(f"{timestamp} / {my_log_line}")


def get_time():
    return datetime.now()


for i in range(10):
    time.sleep(1)
    trace("process step :" + str(i))

