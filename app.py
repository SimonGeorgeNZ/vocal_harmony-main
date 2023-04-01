import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from playsound import playsound
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


@app.route("/", methods=["GET", "POST"])
def load_the_page():
    return render_template(
        "index.html",
        ks=get_data(),
        # sk=pick_your_key(),
        # notes=get_scale_notes(),
    )


@app.route("/harmony/<key>", methods=["POST", "GET"])
def harmony(key):
    picked = mongo.db.keys.find_one({"keySig": key})
    Keynotes = picked["notes"]
    key = picked["keySig"]
    print("one")
    return render_template(
        "index.html",
        # sk=pick_your_key(),
        Keynotes=Keynotes,
        ks=get_data(),
        key=key,
        root=get_root(),
        path=file_path(),
    )


def get_root():
    root = request.form.get("rootSelect")
    if request.method == "POST":
        print(root)
        return root


def file_path():
    if request.method == "POST":
        root = get_root()
        first = "./media/"
        second = ".wav"
        result = first + root + second
        print(result)
        playsound(result)
        return result


if __name__ == "__main__":
    app.run(debug=True)
