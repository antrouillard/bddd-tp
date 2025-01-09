from pymongo.errors import DuplicateKeyError
from python.db import db  # Importer la connexion MongoDB centralisée
from python.auth.tools import hash_sha512  # Import de votre fonction de hachage

# Accès à la collection "membres"
collMembres = db["membres"]
collMatos = db["matos"]
collGroupe = db["groupe"]

def initialize_data():
    """Remplit la base de données avec des utilisateurs initiaux."""
    users = [
        {
            "EMAIL": "jean.dupont@example.com",
            "PASSWORD": hash_sha512("motdepasse"),  # Mot de passe haché
            "TOKEN": None,
            "ISACTIF": True
        },
        {
            "NOM": "Simpson",
            "PRENOM": "Maddie",
            "PASSWORD": hash_sha512("maddie"),  # Mot de passe haché
            "ADRESSE": "13, rue X, VA, 59300",
            "EMAIL": "mad.sim@live.com",
            "GROUPE": "67644cac414760888d79da40",
            "ACTIF?": "actif",
            "TOKEN": None,
        },
        {
            "NOM": "Monroe",
            "PRENOM": "Madison",
            "PASSWORD": hash_sha512('madison'),
            "ADRESSE": "1, rue de la Paix, Lille, 59000",
            "EMAIL": "mad.mon@live.com",
            "GROUPE": "67644cac414760888d79da40",
            "ACTIF?": "client",
            "TOKEN": None,
        }
    ]
    matos = [
        {
            "NUMERO_SERIE": "45ze",
            "MARQUE": "Deal",
            "MODELE": "Zr500",
            "TYPE": "souris",
            "PRIX": "58",
            "GROUPE" :"67644cac414760888d79da40",
        },
        {
            "NUMERO_SERIE": "rùkfgkm8",
            "MARQUE": "SAMSUNG,",
            "MODELE": "GU-563",
            "TYPE": "ecran",
            "PRIX": "752",
            "GROUPE": "67644cac414760888d79da40",
        }
    ]

    groupes = [
        {
            "NUM": 1,
            "NAME": "NOUS",
            "CITY": "LILLE",
            "POSTALCODE": "59000",
        },
        {
            "NUM": 2,
            "NAME": "Groupe 2",
            "CITY": "VA",
            "POSTALCODE": "59300",
        }
    ]

    for user in users:
        # Vérifier si l'utilisateur existe déjà
        if collMembres.find_one({"EMAIL": user["EMAIL"]}):
            print(f"Utilisateur {user['EMAIL']} existe déjà.")
        else:
            try:
                collMembres.insert_one(user)
                print(f"Utilisateur {user['EMAIL']} ajouté.")
            except DuplicateKeyError:
                print(f"Erreur : doublon détecté pour {user['EMAIL']}.")


    for mat in matos:
        # Vérifier si le matos existe déjà
        if collMatos.find_one({"NUMERO_SERIE": mat["NUMERO_SERIE"]}):
            print(f"Matos {mat['NUMERO_SERIE']} existe déjà.")
        else:
            try:
                collMatos.insert_one(mat)
                print(f"Matos {mat['NUMERO_SERIE']} ajouté.")
            except DuplicateKeyError:
                print(f"Erreur : doublon détecté pour {mat['NUMERO_SERIE']}.")


    for groupe in groupes:
        # Vérifier si le groupe existe déjà
        if collGroupe.find_one({"POSTALCODE": groupe["POSTALCODE"]}):
            print(f"Groupe {groupe['POSTALCODE']} existe déjà.")
        else:
            try:
                collGroupe.insert_one(groupe)
                print(f"Groupe {groupe['POSTALCODE']} ajouté.")
            except DuplicateKeyError:
                print(f"Erreur : doublon détecté pour {groupe['POSTALCODE']}.")


if __name__ == "__main__":
    initialize_data()