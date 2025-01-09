
from flask import session

from ..db import db  # Import de la connexion centralisée

def get_collections_commandes():
    """ Accéder à la collection 'command'"""
    return db["commandes"]


def create_commande(matos, groupe: str):
    """Crée un nouveau materiel dans MongoDB."""
    collection = get_collections_commandes()
    commande_data = {
        "MATERIEL": matos,
        "GROUPE": groupe
    }
    if not collection.find_one(commande_data):
        collection.insert_one(commande_data)
    else:
        print("Commande déjà existante")
