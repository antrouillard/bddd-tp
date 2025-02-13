# coding: utf-8

from flask import Blueprint,redirect, render_template, request, session
from .dataMatos import create_matos
from .dataGroup import does_group_exist, create_group
from .dataUser import create_user
from python.auth.data import logged_in
from ..db import getGroupsID


# Créer un Blueprint pour les routes de creation
creat_blueprint = Blueprint('creat', __name__, template_folder="../../templates", static_folder="../static")

@creat_blueprint.route("/user")
def cUser():
    if not logged_in():
        return render_template("/create/success.html",message="Connectez vous !")
    return render_template("create/user.html", data=getGroupsID())

@creat_blueprint.route("/user/add", methods=['POST'])
def pushUser():
    nom: str = request.form["nom"]
    prenom: str = request.form["prenom"]
    motdepasse: str = request.form["motdepasse"]
    adresse: str = request.form["adresse"]
    email: str = request.form["email"]
    groupe: str = request.form["groupe"]
    role: str = request.form["role"]
    if create_user(nom, prenom, motdepasse, adresse, email, groupe, role):
        return render_template("/create/success.html",message="Succès de la requête")
    else:
        return render_template("/create/success.html",message="L'utilisateur existe déjà")


@creat_blueprint.route("/group")
def cGroup():
    if not logged_in():
        return render_template("/create/success.html",message="Connectez vous !")
    return render_template("create/group.html")

@creat_blueprint.route("/group/add", methods=["POST"])
def group_create():
    nomGroupe: str = request.form["nomGroupe"]
    ville: str = request.form["ville"]
    cp: str = request.form["cp"]
    if create_group(nomGroupe, ville,cp):
        return render_template("/create/success.html",message="Succès de la requête")
    else:
        return render_template("/create/success.html",message="Le groupe existe déjà")

@creat_blueprint.route("/matos")
def cMatos():
    if not logged_in():
        return render_template("/create/success.html",message="Connectez vous !")
    return render_template("create/matos.html",data=getGroupsID())

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

    return render_template("/create/success.html")
