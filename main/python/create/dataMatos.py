# coding: utf-8

from flask import session

from ..db import db  # Import de la connexion centralisée

def get_collections_matos():
    """ Accéder à la collection "matos"""
    return db["matos"]


def create_matos(numserie: str, marque: str, modele: str, typeuh: str, prix: str, groupe: str):
    """Crée un nouveau materiel dans MongoDB.
    Retourne 1 si succès 0 sinon
    """
    collection = get_collections_matos()
    matos_data = {
        "NUMERO_SERIE": numserie,
        "MARQUE": marque,
        "MODELE": modele,
        "TYPE": typeuh,
        "PRIX": prix,
        "GROUPE": groupe
    }
    if not db.matos.find_one(matos_data):
        db.matos.insert_one(matos_data)
        return 1
    else:
        print("Matériel déjà existant")
        return 0
