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
    selected_key = request.form.get("keySig")
    sel_key = mongo.db.keys.find_one({"keySig": selected_key})
    return sel_key


def get_scale_notes():
    keyNotes = pick_your_key()
    if request.method == "POST":
        listNotes = keyNotes.get("notes")
        return listNotes


def shuffle():
    notes = get_scale_notes()
    if request.method == "POST":
        print(notes)  # prints correct order#
        x = 0
        while x < 6:
            a = notes.pop(0)
            taken = a
            notes.append(taken)
            x += 1
            print(notes)

    return notes


@app.route("/", methods=["GET", "POST"])
def Load_the_page():
    return render_template(
        "index.html",
        ks=get_data(),
        sk=pick_your_key(),
        notes=get_scale_notes(),
        test=shuffle(),
    )


if __name__ == "__main__":
    app.run(debug=True)
