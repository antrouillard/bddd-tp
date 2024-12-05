from flask import Flask, redirect, render_template

app = Flask(__name__)

@app.route('/')
def bonjour():
    return "<h1>Bonjour</h1>"

if __name__ == '__main__':
    app.run(debug=True)
    
''' 
# coding: utf-8

# Import Flask requirements
from flask import Flask

from .python.secret_key import generate_secret_key

# Create our Flask application object, kind of "global" variable
app = Flask(__name__, template_folder="../templates", static_folder="../static")

app.secret_key = generate_secret_key()

# Import submodules
from . import auth
from . import affichage

from .python.auth.data import logged_in

@app.route("/")
def index():
    if not logged_in():
        return redirect("/login")
    return render_template("InterfaceWEBMAIN.html")
'''   