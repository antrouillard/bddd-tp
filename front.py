# coding: utf-8

# Import Flask requirements
from flask import Flask, redirect

from python.auth.routes import auth_blueprint

# Create our Flask application object, kind of "global" variable
app = Flask(__name__, template_folder="./templates", static_folder="./static")

# Enregistrer le Blueprint
app.register_blueprint(auth_blueprint, url_prefix='/auth')

@app.route('/bonjour')
def bonjour():
    return "<h1>Bonjour</h1>"


@app.route("/")
def index():
    return redirect("/auth/login")

if __name__ == '__main__':
    # Lance le serveur'''
    app.run(debug=True)