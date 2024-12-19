# coding: utf-8

#from  import main
from flask import Blueprint,redirect, render_template, request, session
from python.db import db



# Créer un Blueprint pour les routes d'authentification
disp_blueprint = Blueprint('see', __name__, template_folder="../../templates", static_folder="../../static")

@disp_blueprint.route("/")
def see_wich():
    return render_template("display/choose.html")

@disp_blueprint.route("/matos")
def display_matos():
    """"""
    collection = db["matos"]

    data = list(collection.find())
    return render_template("display/displayMatos.html",data=data)