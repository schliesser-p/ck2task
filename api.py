import flask
from flask import jsonify
from ck2l import get_recepy_dict

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route("/", methods=["GET"])
def home():
    return "<h1> API Test </h1>"

url = "https://www.chefkoch.de/rezepte/745721177147257/Lasagne.html"
recepy = get_recepy_dict(url)

@app.route("/recepy")
def api_all():
    return jsonify(recepy)

app.run()
