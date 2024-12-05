# coding: utf-8

# Import Flask requirements
from flask import Flask, redirect, render_template, url_for


# Create our Flask application object, kind of "global" variable
app = Flask(__name__, template_folder="templates", static_folder="static")

@app.route('/bonjour')
def bonjour():
    return "<h1>Bonjour</h1>"


@app.route("/")
def index():
    return render_template("/home.html")

@app.route("/register")
def register():
    return render_template("/createUser.html")

@app.route("/createGroup")
def createGroup():
    return render_template("/cGroup.html")

@app.route("/addMatos")
def addMatos():
    return render_template("/addMatos.html")


if __name__ == '__main__':
    app.run(debug=True)