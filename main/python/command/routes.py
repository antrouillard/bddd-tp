# coding: utf-8

from flask import Blueprint,redirect, render_template, request, session

from python.db import db


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
