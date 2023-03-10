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


def pick_your_key():
    sel_key = []
    selected_key = request.form.get("keySig")
    sel_key = mongo.db.keys.find_one({"keySig": selected_key})
    return sel_key


# Finds all notes in selected key signature from DB using previous function#
# Used to display all the notes of the scale in "The notes are"#


def get_scale_notes():
    keyNotes = pick_your_key()
    if request.method == "POST":
        listNotes = keyNotes.get("notes")
        return listNotes


@app.route("/", methods=["GET", "POST"])
def load_the_page():
    return render_template(
        "index.html",
        ks=get_data(),
        sk=pick_your_key(),
        notes=get_scale_notes(),
    )


if __name__ == "__main__":
    app.run(debug=True)
