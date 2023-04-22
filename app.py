import os
import wave
from time import sleep
import simpleaudio as sa
from os import path
from flask import Flask, render_template, request, Response, redirect, url_for
from flask_pymongo import PyMongo
from pydub import AudioSegment
from playsound import playsound
from bson.objectid import ObjectId


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
    return render_template(
        "index.html",
        ks=get_data(),
    )


# Gets all info from DB needs the (key) attributed to work


def all_info(key):
    allinfo = mongo.db.keys.find_one({"keySig": key})
    return allinfo


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
    get_notes = all_info(key)
    Keynotes = get_notes["notes"]
    root = request.form.get("rootSelect")
    getHarmonyKeys(key)
    if request.method == "POST":
        filename = f"./media/{root}.wav"
        wave_obj = sa.WaveObject.from_wave_file(filename)
        play_obj = wave_obj.play()
        play_obj.wait_done
    return render_template(
        "root.html",
        root=root,
        key=key,
        ks=ks,
        Keynotes=Keynotes,
    )


@app.route("/root_2/<key>/", methods=["POST", "GET"])
def getHarmonyKeys(key):
    root = request.form.get("rootSelect")
    ks = get_data()
    get_notes = all_info(key)
    Keynotes = get_notes["notes"]
    # titlelist = (
    #     "audio1",
    #     "audio2",
    #     "audio3",
    #     "audio4",
    #     "audio5",
    #     "audio6",
    #     "audio7",
    #     "audio8",
    # )
    harmlist = []
    # counter = 0

    for x in Keynotes:
        harmkeys = request.form.get(x)
        if harmkeys:
            harmlist.append(harmkeys)
    for i in harmlist:
        # counter = counter + 1
        Hstring = "media/{}.wav".format(i)
        print(Hstring)
        wave_obj = sa.WaveObject.from_wave_file(Hstring)
        play_obj = wave_obj.play()
        play_obj.wait_done
        # n = counter
        # titlekey = f"audio{n}"
        # title = titlelist[n - 1]
        # print(title)

        # usedtitles = []
        # usedtitles.append(title)
        # title = AudioSegment.from_file(Hstring)
        # mixed = title.overlay(title).overlay(title).overlay(title)
        # title.export("created/mixed.wav", format="wav")
        # print(Hstring)

        # sleep(0.5)
        # string = "created/mixed.wav"
        # playsound(string)
        # rootfile = f"./media/{root}.wav"
        # filename = "./created/mixed.wav"

        # wave_obj = sa.WaveObject.from_wave_file(rootfile)

    return render_template(
        "root.html",
        key=key,
        ks=ks,
        root=root,
        Keynotes=Keynotes,
        harmlist=harmlist,
    )


# @app.route("/root_3/", methods=["POST", "GET"])
# def getHarmonyKeys2():
#     test1 = "B"
#     test2 = "F#"
#     test3 = "Db"
#     test4 = "G"

#     string1 = "./media/{}.wav".format(test1)
#     string2 = "./media/{}.wav".format(test2)
#     string3 = "./media/{}.wav".format(test3)
#     string4 = "./media/{}.wav".format(test4)

#     audio1 = AudioSegment.from_file(string1)
#     audio2 = AudioSegment.from_file(string2)
#     audio3 = AudioSegment.from_file(string3)
#     audio4 = AudioSegment.from_file(string4)

#     mixed = audio1.overlay(audio2).overlay(audio3).overlay(audio4)

#     mixed.export("./created/mixed.wav", format="wav")  # export mixed  audio file
#     string = "./created/mixed.wav"

#     playsound(string)  # play mixed audio file
#     return render_template(
#         "json.html",
#     )


# @app.route("/json")
# def json():
#     return render_template("json.html")


# @app.route("/background_process_test")
# def background_process_test():
#     print("Hello")
#     return "nothing"


if __name__ == "__main__":
    app.run(debug=True)
