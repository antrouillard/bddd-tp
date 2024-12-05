# coding: utf-8

# Import Flask requirements
from flask import Flask, redirect, render_template

from .python.secret_key import generate_secret_key

# Create our Flask application object, kind of "global" variable
app = Flask(__name__, template_folder="../templates", static_folder="../static")

@app.route('/bonjour')
def bonjour():
    return "<h1>Bonjour</h1>"

app.secret_key = generate_secret_key()

from .python.auth.data import logged_in

@app.route("/")
def index():
    return redirect("/login")

if __name__ == '__main__':
    app.run(debug=True)