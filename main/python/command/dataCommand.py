
from flask import session

from ..auth.tools import current_datetime
from ..auth.data import get_user_id_by_token
from ..db import db  # Import de la connexion centralisée
from bson.objectid import ObjectId

def get_collections_commandes():
    """ Accéder à la collection 'command'"""
    return db["commandes"]


def create_commande(matos, groupe: str):
    """Crée un nouveau materiel dans MongoDB.
    Retourne 1 si succès 0 sinon
    """
    collection = get_collections_commandes()
    idClient = str(get_user_id_by_token(session.get("token"),db["membres"]))
    print(db["membres"].find_one({"_id": ObjectId(idClient)}))
    
    # boucle pour le prix total de la commande
    coll_mat = db["matos"]
    prix = 0
    for mat in matos:
        prix += int(coll_mat.find_one({"_id": ObjectId(mat)},{"_id":False,"PRIX":True})["PRIX"])

    commande_data = {
        "MATERIEL": matos,
        "GROUPE": db["membres"].find_one({"_id": ObjectId(idClient)}).get("GROUPE"),
        "PRIX": prix,
        "CLIENT_ID": str(get_user_id_by_token(session.get("token"),db["membres"])),
        "DATE": current_datetime(),
    }
    if not collection.find_one(commande_data):
        collection.insert_one(commande_data)
        return 1
    else:
        print("Commande déjà existante")
        return 0
