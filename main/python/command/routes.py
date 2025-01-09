# coding: utf-8

from flask import Blueprint,redirect, render_template, request, session

from python.db import db
from .dataCommand import create_commande


# Créer un Blueprint pour les routes de creation
command_blueprint = Blueprint('command', __name__, template_folder="../../templates", static_folder="../../static")

@command_blueprint.route("/create")
def newCommand():

    collGroup = db['groupe']
    dataGroupes = list(collGroup.find())

    collection = db["matos"]

    dataMatos = list(collection.find())
    print(dataMatos)
    
    return render_template("command/create.html",dataGroup=dataGroupes,dataMat=dataMatos)


@command_blueprint.route("/create/add",methods=["POST"])
def creationMatos():
    print("Creation...")
    
    matos = request.form.getlist("matosName")
    groupe: str = request.form.get("groupName")

    create_commande(matos,groupe)

    return "Matériel ajouté"
