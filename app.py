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

# s = request.session()
# s.get("http://httpbin.org/cookies/set", params={"foo": "bar"})
# <Response [200]>
#  s.cookies.keys()
# ['foo']
#  s.get('http://httpbin.org/cookies').json()
# {u'cookies': {u'foo': u'bar'}}
# s.cookies.clear()
# s.cookies.keys()
# []
# s.get('http://httpbin.org/cookies').json()
# {u'cookies': {}}


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


@app.route("/get_key/<key>", methods=["POST", "GET"])
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


@app.route("/root/<key>", methods=["POST", "GET"])
def pick_root(key):
    ks = get_data()
    get_notes = all_info(key)
    Keynotes = get_notes["notes"]
    root = request.form.get("rootSelect")
    if request.method == "POST":
        rootfile = f"media/{root}.wav"
        out_f = AudioSegment.from_file(rootfile)
        play(out_f)
        # wave_obj = sa.WaveObject.from_wave_file(rootfile)
        # root_obj = wave_obj.play()
        # root_obj.wait_done
    return render_template(
        "root.html",
        root=root,
        key=key,
        ks=ks,
        Keynotes=Keynotes,
    )


@app.route("/root_2/<key>", methods=["POST", "GET"])
def getHarmonyKeys(key):
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
    for i in harmlist:
        counter = counter + 1
        Hstring = "media/{}.wav".format(i)
        if counter == 1:
            audio1 = AudioSegment.from_file(Hstring)
            fileroot = f"./media/{root}.wav"
            roottrack = AudioSegment.from_file(fileroot)
            out_f = audio1.overlay(roottrack)
            # mixedroot.export("created/mixed.wav", format="wav")
            if counter == 2:
                audio2 = AudioSegment.from_file(Hstring)
                out_f = out_f.overlay(audio2)
                # mixed.export("created/mixed.wav", format="wav")
            if counter == 3:
                audio3 = AudioSegment.from_file(Hstring)
                out_f = out_f.overlay(audio3)
                # mixed2.replace("created/mixed.wav", format="wav")
            if counter == 4:
                audio4 = AudioSegment.from_file(Hstring)
                out_f = out_f.overlay(audio4)
                # mixed3.export("created/mixed.wav", format="wav")
            if counter == 5:
                audio5 = AudioSegment.from_file(Hstring)
                out_f = out_f.overlay(audio5)
                # mixed4.export("created/mixed.wav", format="wav")
            if counter == 6:
                audio6 = AudioSegment.from_file(Hstring)
                out_f = out_f.overlay(audio6)
                # mixed5.export("created/mixed.wav", format="wav")
            if counter == 7:
                audio7 = AudioSegment.from_file(Hstring)
                out_f = out_f.overlay(audio7)
                # mixed6.export("created/mixed.wav", format="wav")
            # filename = "created/mixed.wav"
            # wave_obj = sa.WaveObject.from_wave_file(filename)
            # play_obj = wave_obj.play()
            # play_obj.wait_done
            play(out_f)

    return render_template(
        "root.html",
        key=key,
        ks=ks,
        root=root,
        Keynotes=Keynotes,
        harmlist=harmlist,
    )


if __name__ == "__main__":
    app.run(debug=True)
