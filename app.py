import os
from flask import Flask, render_template, request
from flask import Flask
from flask_pymongo import PyMongo
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
    return render_template(
        "select_root.html",
        gn=get_notes,
        Keynotes=Keynotes,
        ks=ks,
        key=key,
    )


@app.route("/root/<key>/", methods=["POST", "GET"])
def root(key):
    get_notes = all_info(key)
    Keynotes = get_notes["notes"]
    if request.method == "POST":
        note = request.form.get("rootSelect")
    string = "./media/{}.wav".format(note)
    playsound(string)
    return render_template(
        "root.html",
        key=key,
        Keynotes=Keynotes,
        sk=set_key(key),
        ks=get_data(),
        note=note,
    )
    
# def root_path(key):
#     if request.method == "POST":
#         note=root(key)
#         middle= note
#         start = "./media/"
#         end = ".wav"
#         result = start + middle + end
#         print(result)
#         return result
    

# def play(key):
#     key = set_key(key)
#     key = picked["keySig"]
#     string = "./media/{}.wav".format(key)
#     playsound(string)
#     print(key)
#     return playsound

    
# @app.route("/play_note/<key>", methods=["GET", "POST"])
    # def play_note(key):
    #     picked_root = []
    #     if request.method == "POST":
    #         picked_root = request.form.get("rootSelect")
    #         print([picked_root])
    #         picked = mongo.db.keys.find_one({"keySig": key})
    #         Keynotes = picked["notes"]
    #         print("two")
    #         return render_template("index.html", Keynotes=Keynotes, key=key)


# @app.route("/harmony/<key>", methods=["POST", "GET"])
# def harmony(key):
#     get_notes = all_info(key)
#     return render_template(
#         "index.html",
#         sk=set_key(key),
#         Keynotes=get_notes["notes"],
#         key=set_key(key),
#         ks=get_data(),
#         root=get_root(),
#         path=file_path(),
#     )



# @app.route("/tone/<key>", methods=["POST", "GET"])
# def tone(key):
#     picked = mongo.db.keys.find_one({"keySig": key})
#     Keynotes = picked["notes"]
#     key = picked["keySig"]
#     return render_template(
#         "index.html",
#         ks=get_data(),
#         root=get_root(),
#         harm=get_harm_notes(),
#         key=key,
#         Keynotes=Keynotes,
#     )




# def get_harm(key):
#     picked = mongo.db.keys.find_one({"keySig": key})
#     key = picked["keySig"]
#     Keynotes = picked["notes"]
#     # path = file_path()
#     # print(path)
#     # note = "A"
#     # compare = start + note + end
#     # start = "./media/"
#     # end = ".wav"
#     return Keynotes


# @app.route("/harmony_notes/<key>", methods=["POST", "GET"])
# def get_harm_notes(key):
#     key = set_key(key)
#     get_notes = all_info(key)
#     Keynotes = get_notes["notes"]
#     string = "harmSelect"
#     if request.method == "POST":
#         for x in Keynotes:
#             note = x
#             inputname = string + note
#             print(inputname)
#             formname = request.form.get(inputname)
#             start = "./media/"
#             end = ".wav"
#         new_path = start + formname + end
#         playsound(new_path, block=False)
#         print(formname)
#     return render_template(
#         "index.html",
#         ks=get_data(),
#         Keynotes=Keynotes,
#         key=key,
#     )


# @app.route("/harmony/<key>", methods=["POST", "GET"])
# def try_get(key):
#     picked = mongo.db.keys.find_one({"keySig": key})
#     Keynotes = picked["notes"]
#     key = picked["keySig"]
#     for a in Keynotes:
#         note = a
#         name = "harmSelect"
#         string = name + note
#     if request.method == "POST":
#         Keynotes = picked["notes"]
#         playedNotes = request.form.get("string")
#         print(playedNotes)

#     print(playedNotes)

#     for x in playedNotes:
#         print(x)
#     for a in playedNotes:
#         print(a)
#         print(x)
#         print(compare)
#     return render_template(
#         "index.html",
#         Keynotes=Keynotes,
#         ks=get_data(),
#         key=key,
#     )


if __name__ == "__main__":
    app.run(debug=True)
