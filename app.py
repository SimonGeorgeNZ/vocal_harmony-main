import os
from os import path
import simpleaudio as sa
from flask import Flask, render_template, request, Response, redirect, url_for
from flask_pymongo import PyMongo
from pydub import AudioSegment
from pydub.playback import play

from notes import get_major_scale, get_key_signatures, get_chords


app = Flask(__name__)

key_signatures = get_key_signatures()


def get_key():
    selected_key = request.form["keySignature"]
    return selected_key


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        selected_key = get_key()
        major_scale = get_major_scale(selected_key)

    return render_template(
        "index.html",
        major_scale=major_scale,
        dorian=major_scale[1:] + major_scale[:1],
        phrygian=major_scale[2:] + major_scale[:2],
        lydian=major_scale[3:] + major_scale[:3],
        mixolydian=major_scale[4:] + major_scale[:4],
        aeolian=major_scale[5:] + major_scale[:5],
        locrian=major_scale[6:] + major_scale[:6],
        ks=key_signatures,
        selected_key=selected_key,
        scale=get_scale(),
        p=get_patterns(),
    )


# gets the chord pattern
def get_patterns():
    gc = get_chords()
    return gc


# gets scale
def get_scale():
    selected_key = get_key()
    scale = get_major_scale(selected_key)
    return scale


def chord_notes():
    scale = get_scale()  # Gets scale
    pattern = get_patterns()  # Gets all chord patters
    for key in pattern:  # key gives dic key number ie 1
        chord = pattern[key]  # gives chord pattern [1, 3, 5]
        for each in chord:
            print(".")
            print(chord)
        print(scale[each])
    print(x)
    x = pattern.get(key)
    notes.append(each)
    a = str(pattern[each])
    print(each)
    print(scale[each])
    print(chord)
    a = str(scale[each])
    print(new)
    return scale


if __name__ == "__main__":
    app.run(debug=True)
