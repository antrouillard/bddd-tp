# coding: utf-8

from flask import Blueprint,redirect, render_template, request, session

from python.db import db
from .dataCommand import create_commande
from ..auth.data import get_user_id_by_token
from bson.objectid import ObjectId


# Créer un Blueprint pour les routes de creation
command_blueprint = Blueprint('command', __name__, template_folder="../../templates", static_folder="../../static")

@command_blueprint.route("/create")
def newCommand():

#    print(db["membres"].find_one({"_id": ObjectId('678001b85c564aedf77cca65')}).get("GROUPE"))
    
    collGroup = db['groupe']
    dataGroupes = list(collGroup.find())

    collection = db["matos"]

    dataMatos = list(collection.find())
    print(dataMatos)
    
    return render_template("command/create.html",dataGroup=dataGroupes,dataMat=dataMatos)


@command_blueprint.route("/create/add",methods=["POST"])
def creationCommande():
    print("Creation...")
    
    matos = request.form.getlist("matosName")
    groupe: str = request.form.get("groupName")

    if create_commande(matos,groupe):return redirect("/home")
    else: return "Erreur à la commande"
