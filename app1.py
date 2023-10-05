import os
from os import path
import simpleaudio as sa
from flask import Flask, render_template, request, Response, redirect, url_for
from flask_pymongo import PyMongo
from pydub import AudioSegment
from pydub.playback import play


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


@app.route("/")
def index():
    return render_template("index.html", ks=get_data(), block=True)


# Gets all info from DB needs the (key) attributed to work


def all_info(key):
    allinfo = mongo.db.keys.find_one({"keySig": key})
    return allinfo


# Gets note to harmonise against#


@app.route("/get_key/select_root/<key>", methods=["POST", "GET"])
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


def getchordnumber():
    order = ["1st", "2nd", "3rd", "4th", "5th", "6th", "7th"]
    return order


def getchordtype():
    types = ["Major", "Minor", "Minor", "Major", "Major", "Minor", "Diminished"]
    return types


@app.route("/pick_root/root/<key>", methods=["POST", "GET"])
def pick_root(key):
    order = getchordnumber()
    types = getchordtype()
    chorddatavoice = getchordvoice()
    chorddataname = getchordname()
    # pattern = getchordpattern()
    # typevoice = gettypevoice()
    # typenames = gettypenames()
    ks = get_data()
    get_notes = all_info(key)
    Keynotes = get_notes["notes"]
    root = request.form.get("rootSelect")
    if request.method == "POST":
        if root:
            rootfile = f"media/{root}.wav"
            out_f = AudioSegment.from_file(rootfile)
            # play(out_f)
        else:
            pass

    return render_template(
        "root.html",
        root=root,
        chorddatavoice=chorddatavoice,
        chorddataname=chorddataname,
        key=key,
        ks=ks,
        Keynotes=Keynotes,
        # typevoice=typevoice,
        # typenames=typenames,
        # pattern=pattern,
        order=order,
        types=types,
    )


@app.route("/getHarmonyKeys/root/<key>", methods=["POST", "GET"])
def getHarmonyKeys(key):
    order = getchordnumber()
    types = getchordtype()
    chorddatavoice = getchordvoice()
    chorddataname = getchordname()
    # pattern = getchordpattern()
    # typevoice = gettypevoice()
    # typenames = gettypenames()
    root = request.form.get("rootSelect")
    counter = 0
    ks = get_data()
    get_notes = all_info(key)
    Keynotes = get_notes["notes"]
    harmlist = []

    for x in Keynotes:
        harmkeys = request.form.get(x)
        if harmkeys:
            harmlist.append(harmkeys)
    if len(harmlist) == 0:
        return render_template(
            "root.html",
            key=key,
            ks=ks,
            root=root,
            Keynotes=Keynotes,
            harmlist=harmlist,
            chorddatavoice=chorddatavoice,
            chorddataname=chorddataname,
            # pattern=pattern,
            order=order,
            types=types,
        )
    else:
        for i in harmlist:
            counter = counter + 1
            Hstring = "media/{}.wav".format(i)
            if counter == 1:
                fileroot = f"./media/{root}.wav"
                roottrack = AudioSegment.from_file(fileroot)
                audio1 = AudioSegment.from_file(Hstring)
                out_f = audio1.overlay(roottrack)
            if counter == 2:
                audio2 = AudioSegment.from_file(Hstring)
                out_f = out_f.overlay(audio2)
            if counter == 3:
                audio3 = AudioSegment.from_file(Hstring)
                out_f = out_f.overlay(audio3)
            if counter == 4:
                audio4 = AudioSegment.from_file(Hstring)
                out_f = out_f.overlay(audio4)
            if counter == 5:
                audio5 = AudioSegment.from_file(Hstring)
                out_f = out_f.overlay(audio5)
            if counter == 6:
                audio6 = AudioSegment.from_file(Hstring)
                out_f = out_f.overlay(audio6)
            if counter == 7:
                audio7 = AudioSegment.from_file(Hstring)
                out_f = out_f.overlay(audio7)
        play(out_f)

        return render_template(
            "root.html",
            key=key,
            ks=ks,
            root=root,
            Keynotes=Keynotes,
            harmlist=harmlist,
            # typevoice=typevoice,
            # typenames=typenames,
            # pattern=pattern,
            order=order,
            chorddatavoice=chorddatavoice,
            chorddataname=chorddataname,
            types=types,
        )


def gettypenames():
    typenames = [
        ("Perfect 2nd"),
        ("Perfect 4th"),
        ("Perfect 5th"),
        ("Perfect 6th"),
        ("Major triad"),
        ("Minor triad"),
        ("Diminished"),
        ("Augmented"),
        ("Major sixth"),
        ("Diminished 7th"),
        ("Half diminished"),
        ("Augmented 7th"),
    ]

    return typenames


# def gettypevoice():
#     typevoice = [
#         ((0, 2), (0, 5), (0, 7), (0, 9)),
#         ((0, 4, 7), (0, 3, 7), (0, 3, 6), (0, 4, 8)),
#         ((0, 4, 7, 9), (0, 3, 6, 9), (0, 3, 6, 10), (0, 4, 8, 10)),
#     ]

#     return typevoice


def get_root():
    root = request.form.get("getRoot")
    return root


def getchordpattern():
    harmchord = request.form.get("chordSelect")
    return harmchord


def getchordvoice():
    type_voice = [
        [
            "0, 2",
            "0, 5",
            "0, 7",
            "0, 9",
        ],
        [
            "0, 4, 7",
            "0, 3, 7",
            "0, 3, 6",
            "0, 4, 8",
        ],
        [
            "0, 4, 7, 9",
            "0, 3, 6, 9",
            "0, 3, 6, 10",
            "0, 4, 8, 10",
        ],
    ]
    return type_voice


def getchordname():
    type_names = (
        [
            "Perfect 2nd",
            "Perfect 4th",
            "Perfect 5th",
            "Perfect 6th",
        ],
        [
            "Major triad",
            "Minor triad",
            "Diminished",
            "Augmented",
        ],
        [
            "Major sixth",
            "Diminished 7th",
            "Half diminished",
            "Augmented 7th",
        ],
    )

    return type_names


@app.route("/commonharms/root/<key>/", methods=["POST", "GET"])
def commonharms(key):
    chorddatavoice = getchordvoice()
    chorddataname = getchordname()
    root = get_root()
    ks = get_data()
    order = getchordnumber()
    types = getchordtype()
    pattern = getchordpattern()

    # function gets value from form#

    notes = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
    sharpKeys = ["A", "B", "C", "D", "E", "F", "G"]
    notes2 = ["A", "Bb", "B", "C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab"]
    flatKeys = ["Bb", "Db", "Eb", "Gb", "Ab"]
    newharm = []
    counter = 0
    get_notes = all_info(key)
    Keynotes = get_notes["notes"]
    # times = len(chordselect)

    for x in chorddatavoice:
        for y in x:
            y = str(y)
            if pattern == y:
                if pattern:
                    newpattern = pattern.split(",")

                    for i in sharpKeys:
                        if root == i:
                            # print(i)
                            start = notes.index(i)
                            end = len(notes)
                            notes = notes[start:end] + notes[0:start]
                        else:
                            for m in flatKeys:
                                if root == m:
                                    print(m)
                                    start = notes2.index(m)
                                    end = len(notes2)
                                    notes = notes2[start:end] + notes2[0:start]
                            # print(notes)
                for d in newpattern:
                    add = int(d)
                    each = notes[add]
                    newharm.append(each)
    print(newharm)
    for a in newharm:
        print(a)
        counter = counter + 1
        Hstring = "media/{}.wav".format(a)
        # print(Hstring)
        if counter == 1:
            audio1 = AudioSegment.from_file(Hstring)
        if counter == 2:
            audio2 = AudioSegment.from_file(Hstring)
            out_f = audio1.overlay(audio2)
            if counter == 3:
                audio3 = AudioSegment.from_file(Hstring)
                out_f = out_f.overlay(audio3)
            if counter == 4:
                audio4 = AudioSegment.from_file(Hstring)
                out_f = out_f.overlay(audio4)
            # play(out_f)
    return render_template(
        "root.html",
        chorddatavoice=chorddatavoice,
        chorddataname=chorddataname,
        ks=ks,
        key=key,
        root=root,
        Keynotes=Keynotes,
        pattern=pattern,
        order=order,
        types=types,
    )


if __name__ == "__main__":
    app.run(debug=True)
