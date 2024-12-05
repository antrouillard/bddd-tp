# coding: utf-8

#from  import main


from .tools import hash_sha512, token_for

# TO DO : Interroger l'endroit où l'on stocke les utilisateurs pour créer / vérifier
# from .data import is_credential_correct, set_token, create_user

from flask import Blueprint,redirect, render_template, request, session

# Créer un Blueprint pour les routes d'authentification
auth_blueprint = Blueprint('auth', __name__, template_folder="../../templates", static_folder="../static")

@auth_blueprint.route("/login")
def login():
# Pas besoin d'indiquer que le fichier index.html est dans le sous-dossier templates: c'est implicite avec la fonction render_template
    return render_template("auth/login.html")

'''
@app.route("/login/auth", methods=["POST"])
def login_auth():
    login: str = request.form["login"]
    password: str = request.form["password"]
    hashed_password: str = hash_sha512(password)
    # TO DO
    auth_ok: bool = is_credential_correct(login, hashed_password)
    if auth_ok:
        # On créer un token pour l'utilisateur saisi dans login
        user_token: str = token_for(login)
        # On met à jour le token dans la base de donnée
        # TO DO
        set_token(login, user_token)
        # On met à jour le cache client pour ajouter le token:
        session["token"]= user_token
        return redirect("/")
    else:
        return "Auth failed !"
        
@app.route("/login/create", methods=["POST"])
def login_create():
    login: str = request.form["login"]
    password: str = request.form["password"]
    nomVillage : str = request.form["nomVillage"]
    hashed_password: str = hash_sha512(password)
    # TO DO
    auth_ok: bool = is_credential_correct(login, hashed_password)
    if auth_ok == False:
        user_token: str = token_for(login)
        # TO DO
        create_user(login,hashed_password,user_token,nomVillage)
        session["token"]= user_token
        return "Compte créé"
    else :
        return "Le compte existe déja"
        '''