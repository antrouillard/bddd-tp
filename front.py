from flask import Flask

app = Flask(__name__)

@app.route('/')
def bonjour():
    return "<h1>Bonjour</h1>"

if __name__ == '__main__':
    app.run(debug=True)
    
    
# coding: utf-8

# Import Flask requirements
from flask import Flask

from .secret_key import generate_secret_key

# Create our Flask application object, kind of "global" variable
app = Flask(__name__, template_folder="../templates", static_folder="../static")

app.secret_key = generate_secret_key()

# Import PostgreSQL requirements and prepare db connection
import psycopg2
con = psycopg2.connect(host='localhost', user='management_game', password='ant', dbname='bd')

# Import submodules
from . import auth
from . import affichage

# Load main page
from . import index