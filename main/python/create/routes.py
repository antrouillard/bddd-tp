# coding: utf-8

from flask import Blueprint,redirect, render_template, request, session
from .dataMatos import create_matos

# Créer un Blueprint pour les routes de creation
creat_blueprint = Blueprint('creat', __name__, template_folder="../../templates", static_folder="../static")

@creat_blueprint.route("/user")
def cUser():
    return render_template("create/user.html")

@creat_blueprint.route("/group")
def cGroup():
    return render_template("create/group.html")

@creat_blueprint.route("/matos")
def cMatos():
    return render_template("create/matos.html")

@creat_blueprint.route("/matos/add",methods=["POST"])
def creationMatos():
    print("Creation...")
    numserie: str = request.form["numeroSerie"]
    marque: str = request.form["marque"]
    modele: str = request.form["modele"]
    typeuh: str = request.form["type"]
    prix: str = request.form["prix"]
    groupe: str = request.form["groupe"]

    create_matos(numserie,marque,modele,typeuh,prix,groupe)

    return "Matériel ajouté"
