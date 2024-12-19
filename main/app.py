# coding: utf-8

# Import Flask requirements
from flask import Flask, redirect, render_template

#import pymongo
from pymongo import MongoClient

import os
from python.auth.routes import auth_blueprint
from python.create.routes import creat_blueprint
from python.auth.data import logged_in
from python.init_db import initialize_data  # Import de l'initialisation MongoDB


# Connexion à MongoDB
client = MongoClient('mongodb://mongodb:27017/')
db = client.mydatabase

# Initialisation de la base de données au démarrage
initialize_data()

# Create our Flask application object, kind of "global" variable
app = Flask(__name__, template_folder="./templates", static_folder="./static")


app.secret_key = os.urandom(24)  # Génère une clé aléatoire à chaque démarrage (non persistante)

# Enregistrer le Blueprint
app.register_blueprint(auth_blueprint, url_prefix='/auth')
app.register_blueprint(creat_blueprint, url_prefix='/create')

@app.route('/bonjour')
def bonjour():
    return "<h1>Bonjour</h1>"

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/profile")
def profile():
    if not logged_in():
        return redirect("/auth/login")
    return "Utilisateur connecté avec succès !"

@app.route("/")
def index():
    if not logged_in():
        return redirect("/auth/login")
    return redirect("/home")
if __name__ == '__main__':
    # Lance le serveur'''
    app.run(host='0.0.0.0', port=5000, debug=True)

