# coding: utf-8

from flask import session

from ..db import db  # Import de la connexion centralisée


# coding: utf-8

from flask import session

from ..db import db  # Import de la connexion centralisée



def get_collections_group():
    """ Accéder à la collection "groupe"""
    return db["groupe"]


def get_name_city_pc(nameGroup: str, cityGroup: str,postalCodeGroup: str):
    """Recherche un utilisateur dans MongoDB en fonction de son login et de son mot de passe haché"""
    collection = get_collections_group()
    return collection.find_one({"nomGroupe": nameGroup, "ville": cityGroup, "cp": postalCodeGroup})


def does_group_exist(nameGroup: str, cityGroup: str,postalCodeGroup: str) -> bool:
    """# Vérifie si les identifiants sont corrects"""
    return get_name_city_pc(nameGroup, cityGroup,postalCodeGroup) is not None

def generate_num_group(collection):
    """ Retourne le nombre de groupes dans MongoDB +1"""
    return collection.count_documents({})+1

def create_group(nameGroup: str, cityGroup: str,postalCodeGroup: str) -> bool:
    """Crée un nouvel utilisateur dans MongoDB."""
    collection = get_collections_group()
    num_group:int = generate_num_group(collection)
    group_data = {
        "NUM": num_group,
        "NAME": nameGroup,
        "CITY": cityGroup,
        "POSTALCODE": postalCodeGroup,
    }
    if collection.count_documents({"NAME": nameGroup, "CITY": cityGroup, "POSTALCODE": postalCodeGroup, }) == 0:
        collection.insert_one(group_data)
        return True
    else:
        return False


