# coding: utf-8

#from  import main
from .tools import hash_sha512, token_for
from .data import is_credential_correct, set_token, create_user, log_off
from flask import Blueprint,redirect, render_template, request, session
from python.db import db




# Créer un Blueprint pour les routes d'authentification
auth_blueprint = Blueprint('auth', __name__, template_folder="../../templates", static_folder="../../static")

@auth_blueprint.route("/login")
def login():
# Pas besoin d'indiquer que le fichier index.html est dans le sous-dossier templates: c'est implicite avec la fonction render_template
    return render_template("auth/login.html")


@auth_blueprint.route("/login/auth", methods=["POST"])
def login_auth():
    login: str = request.form["email"]
    password: str = request.form["password"]
    hashed_password: str = hash_sha512(password)
    if is_credential_correct(login, hashed_password):

        user_token: str = token_for(login)      # On créer un token pour l'utilisateur saisi dans login
        set_token(login, user_token)            # On met à jour le token dans la base de donnée
        session["token"]= user_token            # On met à jour le cache client pour ajouter le token:

        return redirect("/")
    else:
        return render_template("create/success.html",message="Authentification échouée")
        
@auth_blueprint.route("/login/create", methods=["POST"])
def login_create():
    login: str = request.form["login"]
    password: str = request.form["password"]
    hashed_password: str = hash_sha512(password)
    if not is_credential_correct(login, hashed_password):
        user_token: str = token_for(login)
        create_user(login,hashed_password,user_token)
        session["token"]= user_token
        return render_template("create/success.html",message="Compte créé !")
    else :
        return render_template("create/success.html",message="Compte déjà existant")


@auth_blueprint.route("/logout")
def logout():
    print(session["SecureCookieSession"]) 
    if session["token"] is not None:
        log_off(session["token"])
        return redirect("/auth/login")
    return redirect("/home")

@auth_blueprint.route("/inscription")
def inscription():
    # Page pour afficher le formulaire d'inscription (inscription.html)
    return render_template("auth/inscription.html")

@auth_blueprint.route("/membre/add", methods=["POST"])
def add_membre():
    collection = db["membres"]
    nom = request.form.get("nom")
    prenom = request.form.get("prenom")
    adresse = request.form.get("adresse")
    email = request.form.get("email")
    groupe = request.form.get("groupe")
    role = request.form.get("role")

    user = {
        "NOM": nom,
        "PRENOM": prenom,
        "ADRESSE": adresse,
        "EMAIL": email,
        "GROUPE": groupe,
        "ROLE": role,
        "TOKEN": None
    }

    try:
        collection.insert_one(user)
        print(f"Utilisateur {email} ajouté dans la base de données.")
    except DuplicateKeyError:
        print(f"Erreur : L'utilisateur {email} existe déjà.")
        return render_template("create/success.html",message="L'utilisateur existe déjà")

    return render_template("create/success.html",message="Utilisateur ajouté")
