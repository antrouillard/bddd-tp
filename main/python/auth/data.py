# coding: utf-8

from flask import session

from ..db import db  # Import de la connexion centralisée



def get_collections_user():
    """ Accéder à la collection "membres"""
    return db["membres"]


def get_login_psswrd(login: str, hashed_password: str):
    """Recherche un utilisateur dans MongoDB en fonction de son login et de son mot de passe haché"""
    collection = get_collections_user()
    return collection.find_one({"EMAIL": login, "PASSWORD": hashed_password})


def is_credential_correct(login: str, hashed_password: str) -> bool:
    """# Vérifie si les identifiants sont corrects"""
    return get_login_psswrd(login, hashed_password) is not None


def set_token(login: str, token: str):
    """Met à jour le jeton d'un utilisateur dans MongoDB."""
    collection = get_collections_user()
    collection.update_one({"EMAIL": login}, {"$set": {"TOKEN": token}})
    

def check_token_validity(token: str):
    """Vérifie si le jeton est valide."""
    collection = get_collections_user()
    return collection.find_one({"TOKEN": token}) is not None



def create_user(login: str, password: str, token: str, nomVillage: str):
    """Crée un nouvel utilisateur dans MongoDB."""
    collection = get_collections_user()
    user_data = {
        "EMAIL": login,
        "PASSWORD": password,
        "TOKEN": token,
        "VILLAGE": nomVillage,
    }
    collection.insert_one(user_data)


def get_user_id_by_token(token: str, collection):
    """Récupère l'ID d'utilisateur associé à un jeton."""

    user = collection.find_one({"TOKEN": token}, {"_id": 1})
    return user["_id"] if user else None


def logged_in() -> bool:
    """Vérifie si l'utilisateur est connecté via le token stocké dans la session."""
    token: str = session.get("token", None)
    
    if token:
        return check_token_validity(token)
    return False
