# coding: utf-8

#from  import main
from flask import Blueprint,redirect, render_template, request, session
from python.db import db
from python.auth.data import logged_in
from bson.objectid import ObjectId


# Créer un Blueprint pour les routes d'authentification
disp_blueprint = Blueprint('see', __name__, template_folder="../../templates", static_folder="../../static")

@disp_blueprint.route("/")
def see_wich():
    if not logged_in():
        return render_template("create/success.html",message="Connectez vous !")
    return render_template("display/choose.html")

@disp_blueprint.route("/matos")
def display_matos():
    """"""
    if not logged_in():
        return render_template("create/success.html",message="Connectez vous !")

    collection = db["matos"]

    data = list(collection.find())
    return render_template("display/displayMatos.html",data=data)

@disp_blueprint.route("/members")
def display_members():
    """"""
    if not logged_in():
        return render_template("create/success.html",message="Connectez vous !")

    collection = db["membres"]

    data = list(collection.find({},{"PASSWORD":False, "TOKEN":False}))
    return render_template("display/displayUsers.html",data=data)


@disp_blueprint.route("/groups")
def display_groups():
    """"""
    if not logged_in():
        return render_template("create/success.html",message="Connectez vous !")
        
    collection = db["groupe"]

    data = list(collection.find())
    return render_template("display/displayGroups.html",data=data)


@disp_blueprint.route("/commandes")
def display_commandes():
    """"""
    if not logged_in():
        return render_template("create/success.html",message="Connectez vous !")
        
    collection = db["commandes"]
    collGroupe = db["groupe"]
    collMatos = db["matos"]
    collMembres = db["membres"]


    data = list(collection.find({},{"_id":False}))
    materialS=[]
    groupeNames = []
    clientNames = []
    print(data)
    for dat in data:
        materialNames = []
        for mat in dat["MATERIEL"]:
            matComplet = collMatos.find_one({"_id":ObjectId(mat)})
            materialNames.append(matComplet["MARQUE"]+" "+matComplet["MODELE"])
        materialS.append(materialNames) 
        groupeNames.append(collGroupe.find_one({"_id":ObjectId(dat["GROUPE"])}).get("NAME"))
        client = collMembres.find_one({"_id":ObjectId(dat["CLIENT_ID"])},{"_id":False,"PRENOM":True,"NOM":True})
        clientNames.append(client["PRENOM"]+" "+client["NOM"])

    for i in range(len(data)):
        data[i]["MATERIEL"] = materialS[i]
        data[i]["GROUPE"] = groupeNames[i]
        data[i]["CLIENT_ID"] = clientNames[i]

    return render_template("display/displayCommandes.html",data=data)