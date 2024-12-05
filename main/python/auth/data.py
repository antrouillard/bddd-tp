# coding: utf-8

from flask import session

def get_collections_user(client):
    db = client["assodb"]
    collection = db["membres"]
    
    return collection

# Recherche un utilisateur dans MongoDB en fonction de son login et de son mot de passe haché.
def get_login_psswrd(login: str, hashed_password: str, collection):
    resultats = collection.find_one({"EMAIL": login, "PASSWORD": hashed_password})
    
    return resultats

# Vérifie si les identifiants sont corrects.
def is_credential_correct(login: str, hashed_password: str, collection) -> bool:
    res = get_login_psswrd(login, hashed_password, collection)
    
    return res is not None

# Met à jour le jeton d'un utilisateur dans MongoDB.
def set_token(login: str, token: str, collection): 

    collection.update_one({"EMAIL": login}, {"$set": {"TOKEN": token}})
    
# Vérifie si le jeton est valide.
def check_token_validity(token: str, collection):
    res = collection.find_one({"TOKEN": token})
    
    return res is not None

# Crée un nouvel utilisateur dans MongoDB.
def create_user(login: str, password: str, token: str, nomVillage: str, collection):
    user_data = {
        "EMAIL": login,
        "PASSWORD": password,
        "TOKEN": token,
        "VILLAGE": nomVillage,
    }
    collection.insert_one(user_data)

# Récupère l'ID d'utilisateur associé à un jeton.
def get_user_id_by_token(token: str, collection):
    
    user = collection.find_one({"TOKEN": token}, {"_id": 1})
    
    return user["_id"] if user else None

# Vérifie si l'utilisateur est connecté via le token stocké dans la session.
def logged_in(client) -> bool:
    token: str = session.get("token", None)
    
    if token:
        return check_token_validity(token, client)
    
    return False
