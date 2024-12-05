# coding: utf-8

# Import Flask requirements
from flask import Flask, redirect, render_template

from python.auth.routes import auth_blueprint
from python.create.routes import creat_blueprint

from pymongo import MongoClient

from python.auth.data import logged_in

client = MongoClient("mongodb://localhost:27017/")

# Create our Flask application object, kind of "global" variable
app = Flask(__name__, template_folder="./templates", static_folder="./static")

# Enregistrer le Blueprint
app.register_blueprint(auth_blueprint, url_prefix='/auth')
app.register_blueprint(creat_blueprint, url_prefix='/create')

@app.route('/bonjour')
def bonjour():
    return "<h1>Bonjour</h1>"

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/")
def index():
    if not logged_in(client):
        return redirect("/auth/login")
    return redirect("/home")
if __name__ == '__main__':
    # Lance le serveur'''
    app.run(debug=True)