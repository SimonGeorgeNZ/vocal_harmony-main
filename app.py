import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
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

db = mongo.db.keys


def get_data():
    key_Sig = list(mongo.db.keys.find())
    return key_Sig


def pick_your_key():
    sel_key = []
    if request.method == "POST":
        selected_key = request.form.get("keySig")
        sel_key = mongo.db.keys.find_one({"keySig": selected_key})
    return sel_key


def get_scale_notes():
    keyNotes = pick_your_key()
    if request.method == "POST":
        listNotes = keyNotes.get("notes")
        noteString = ", ".join(listNotes)
        return noteString


@app.route("/", methods=["GET", "POST"])
def Load_the_page():
    sel_key = pick_your_key()
    key_Sig = get_data()
    noteString = get_scale_notes()
    return render_template("index.html", ks=key_Sig, sk=sel_key, notes=noteString)


if __name__ == "__main__":
    app.run(debug=True)
