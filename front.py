from flask import Flask

app = Flask(__name__)

@app.route('/')
def bonjour():
    return "<h1>Bonjour</h1>"

if __name__ == '__main__':
    app.run(debug=True)