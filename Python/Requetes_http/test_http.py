# reçu la requete sur webhook.site https://webhook.site/#!/view/fb62cb69-0d00-4cfd-a26f-8e242a3695f2/6a7a0039-9890-4e06-9c22-3de64822150f/1
# Pour tester des requetes : https://aureliedombre-1375263.postman.co/workspace/12fac99c-452d-4a92-88d2-affd939f150f/request/54229298-18fdc3cd-de1a-48e2-8a4c-67a71a6ce3f6


import requests
import time

webhook_url = "	https://webhook.site/fb62cb69-0d00-4cfd-a26f-8e242a3695f2"

while True:
    try:
        data = {
            "users": 10,
            "server_load": 75,
            "username": "Aurelie"
        }

        response = requests.post(webhook_url, json=data)

        print("Requête envoyée !")
        print("Status:", response.status_code)

        time.sleep(60)

    except Exception as e:
        print(f"Erreur : {e}")