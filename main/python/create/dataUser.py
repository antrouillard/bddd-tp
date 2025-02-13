# coding: utf-8

from flask import session
from python.auth.tools import hash_sha512

from ..db import db  # Import de la connexion centralisée

def get_collections_membres():
    """ Accéder à la collection "matos"""
    return db["membres"]


def create_user(nom : str, prenom : str, motdepasse : str, adresse : str, email : str, groupe : str, role : str):
    """Crée un nouveau materiel dans MongoDB.
    Retourne 1 si succès 0 sinon
    """
    collection = get_collections_membres()
    user_data = {
        "NOM": nom,
        "PRENOM": prenom,
        "PASSWORD": hash_sha512(motdepasse),  # Mot de passe haché
        "ADRESSE": adresse,
        "EMAIL": email,
        "GROUPE": groupe,
        "ACTIF?": role,
        "TOKEN": None,
    }
    if not collection.find_one(user_data):
        collection.insert_one(user_data)
        return 1
    else:
        print("User déjà existant")
        return 0
