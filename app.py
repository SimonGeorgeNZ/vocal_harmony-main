import os
from flask import Flask, render_template, request
from flask import Flask
from flask_pymongo import PyMongo
from playsound import playsound
from bson.objectid import ObjectId
from os import path


if path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = "vocal_harmony"
app.config["MONGO_URI"] = os.getenv("MONGO_URI")


mongo = PyMongo(app)

MONGO_URI = os.environ.get("MONGO_URI")
MONGO_DBNAME = os.environ.get("MONGO_DBNAME")


# Finds all keys in Mongo and displays them in the dropdown menu#
# Adds the keySig attribute from DB as the buttons value#


def get_data():
    key_Sig = list(mongo.db.keys.find())
    return key_Sig


# Gets value (keySig) from form wrapped around dropdown and finds key document in DB that matches key selection#
# Used to display specific key note in "Your key is"#


def set_key(key):
    info = all_info(key)
    key = info["keySig"]
    return key


@app.route("/", methods=["GET", "POST"])
def load_the_page():
    return render_template(
        "index.html",
        ks=get_data(),
    )


# Gets all info from DB needs the (key) attributed to work


def all_info(key):
    all_info = mongo.db.keys.find_one({"keySig": key})
    return all_info


# Gets note to harmonise against#


@app.route("/get_key/<key>/", methods=["POST", "GET"])
def get_key(key):
    get_notes = all_info(key)
    Keynotes = get_notes["notes"]
    key = set_key(key)
    ks = get_data()
    root = request.form.get("rootSelect")
    return render_template(
        "select_root.html",
        Keynotes=Keynotes,
        ks=ks,
        key=key,
        root=root,
    )


@app.route("/root/<key>/", methods=["POST", "GET"])
def pick_root(key):
    ks = get_data()
    root = request.form.get("rootSelect")
    get_notes = all_info(key)
    Keynotes = get_notes["notes"]
    if request.method == "POST":
        string = "./media/{}.wav".format(root)
        # playsound(string)
    return render_template(
        "root.html",
        key=key,
        ks=ks,
        Keynotes=Keynotes,
        root=root,
        harms=harmonykeys(Keynotes),
    )


@app.route("/root/<key>/", methods=["POST", "GET"])
def harmonykeys(Keynotes):
    harmlist = []
    counter = 0
    for x in Keynotes:
        harmkeys = request.form.get(x)
        if harmkeys:
            string = "./media/{}.wav".format(harmkeys)
            harmlist.append(string)
    for i in harmlist:
        counter = counter + 1
    print(counter)
    print(harmlist)
    return render_template(
        "root.html",
        Keynotes=Keynotes,
    )


if __name__ == "__main__":
    app.run(debug=True)
