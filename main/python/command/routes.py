# coding: utf-8

from flask import Blueprint,redirect, render_template, request, session

from python.db import db


# Créer un Blueprint pour les routes de creation
command_blueprint = Blueprint('command', __name__, template_folder="../../templates", static_folder="../../static")

@command_blueprint.route("/create")
def newCommand():

    groupes = db['group']
    dataGroupes = list(groupes.find())

    matos = db['matos']
    dataMatos = list(matos.find())

    
    return render_template("command/create.html",dataGroup=dataGroupes,dataMat=dataMatos)
