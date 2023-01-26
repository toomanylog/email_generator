import random
import string
import os
import ctypes
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor
import names
from functools import partial

# Pour mettre à jour le titre de la fenêtre
def update_title(title):
    ctypes.windll.kernel32.SetConsoleTitleW(title)

# Nombre d'adresses générées par l'utilisateur
quantity = int(input("Choisissez un nombre d'adresses à générer: "))

# Nombre de threads choisis par l'utilisateur
nb_threads = int(input("Choisissez un nombre de threads: "))

# Générer une adresse email aléatoire
def generate_email():
    prenom = names.get_first_name()
    nom = names.get_last_name()
    num = random.randint(0, 99)
    if num < 10:
        num = "0" + str(num)
    return f"{prenom}.{nom}{num}@hotmail.fr"

# Création du dossier pour stocker les résultats
if not os.path.exists("Emails"):
    os.mkdir("Emails")

# Nom du fichier pour stocker les résultats
filename = f"Emails_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"
filepath = os.path.join("Emails", filename)

# Ecriture des résultats dans le fichier
with open(filepath, "w") as f:
    with ThreadPoolExecutor(max_workers=nb_threads) as executor:
        # Code pour afficher l'avancement de la génération
        for i in range(quantity):
            email = generate_email()
            f.write(email + "\n")
            update_title(f"Génération des adresses email - {i+1}/{quantity}")
            print(f"Adresse générée: {email}") # Affiche les adresses générées en temps réel sur la console

print(f"Les adresses ont été générées et enregistrées dans le fichier {filename}.")
