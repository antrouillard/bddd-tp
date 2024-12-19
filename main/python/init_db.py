from pymongo.errors import DuplicateKeyError
from python.db import db  # Importer la connexion MongoDB centralisée
from python.auth.tools import hash_sha512  # Import de votre fonction de hachage

# Accès à la collection "membres"
collection = db["membres"]

def initialize_data():
    """Remplit la base de données avec des utilisateurs initiaux."""
    users = [
        {
            "EMAIL": "jean.dupont@example.com",
            "PASSWORD": hash_sha512("motdepasse"),  # Mot de passe haché
            "TOKEN": None,
            "VILLAGE": "Village Test"
        },
        {
            "EMAIL": "alice@example.com",
            "PASSWORD": hash_sha512("123456"),  # Mot de passe haché
            "TOKEN": None,
            "VILLAGE": "Village Alice"
        }
    ]

    for user in users:
        # Vérifier si l'utilisateur existe déjà
        if collection.find_one({"EMAIL": user["EMAIL"]}):
            print(f"Utilisateur {user['EMAIL']} existe déjà.")
        else:
            try:
                collection.insert_one(user)
                print(f"Utilisateur {user['EMAIL']} ajouté.")
            except DuplicateKeyError:
                print(f"Erreur : doublon détecté pour {user['EMAIL']}.")

if __name__ == "__main__":
    initialize_data()