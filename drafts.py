""" from pydub import AudioSegment
from pydub.playback import play

# _notes = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]

# two2nd = [0, 2]
# two4th = [0, 5]
# two5th = [0, 7]
# three3rd = [0, 4, 7]
# threemin3 = [0, 3, 7]
# three5th = [0, 7, 9]
# diminished = [0, 3, 6]
# dim7th = [0, 3, 6, 9]
# halfdim = [0, 3, 6, 10]
# augmented = [0, 4, 8]
# aug7th = [0, 4, 8, 10]


# userinput = "C"
# chordselect = aug7th


# def commonharms(userinput, chordselect):
#     newharm = []
#     notes = _notes
#     counter = 0
#     root = userinput
#     # times = len(chordselect)
#     for i in notes:
#         if root == i:
#             start = notes.index(i)
#             end = len(notes)
#             notes = notes[start:end] + notes[0:start]
#             for d in chordselect:
#                 each = notes[d]
#                 newharm.append(each)
#                 # print(newharm)
#     for a in newharm:
#         counter = counter + 1
#         Hstring = "media/{}.wav".format(a)
#         # print(Hstring)
#         if counter == 1:
#             audio1 = AudioSegment.from_file(Hstring)
#             print(counter)
#             print(a)
#             print(Hstring)
#         if counter == 2:
#             print(counter)
#             print(a)
#             print(Hstring)
#             audio2 = AudioSegment.from_file(Hstring)
#             out_f = audio1.overlay(audio2)
#         if counter == 3:
#             print(counter)
#             print(a)
#             print(Hstring)
#             audio3 = AudioSegment.from_file(Hstring)
#             out_f = out_f.overlay(audio3)
#         if counter == 4:
#             print(counter)
#             print(a)
#             print(Hstring)
#             audio4 = AudioSegment.from_file(Hstring)
#             out_f = out_f.overlay(audio4)
#     play(out_f)
#     return userinput, chordselect

# typenames = [
#     "two2nd",
#     "two4th",
#     "two5th",
#     "three3rd",
#     "threemin3",
#     "three5th",
#     "diminished",
#     "dim7th",
#     "halfdim",
#     "augmented",
#     "aug7th",
# ]
# typevoice = [
#     [0, 2],
#     [0, 5],
#     [0, 7],
#     [0, 4, 7],
#     [0, 3, 7],
#     [0, 7, 9],
#     [0, 3, 6],
#     [0, 3, 6, 9],
#     [0, 3, 6, 10],
#     [0, 4, 8],
#     [0, 4, 8, 10],
# ]

 chordtypes = dict(
    two2nd=[0, 2],
    two4th=[0, 5],
    two5th=[0, 7],
    three3rd=[0, 4, 7],
    threemin3=[0, 3, 7],
    three5th=[0, 7, 9],
    diminished=[0, 3, 6],
    dim7th=[0, 3, 6, 9],
    halfdim=[0, 3, 6, 10],
    augmented=[0, 4, 8],
    aug7th=[0, 4, 8, 10],
)

for a in chordtypes:
    print(a)


def gettypevoice_1():
    typevoice_1 = [[0, 2], [0, 5], [0, 7], [0, 9]]

    return typevoice_1


def gettypevoice_2():
    typevoice_2 = [[0, 4, 7], [0, 3, 7], [0, 3, 6], [0, 4, 8]]
    return typevoice_2


def gettypevoice_3():
    typevoice_3 = [[0, 4, 7, 9], [0, 3, 6, 9], [0, 3, 6, 10], [0, 4, 8, 10]]

    return typevoice_3
 """


# Your Python function to get scale and chords goes here


def get_key_signatures():
    return ["C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab", "A", "Bb", "B"]


@app.route("/", methods=["GET", "POST"])
def index():
    key_signatures = get_key_signatures()

    if request.method == "POST":
        selected_key = request.form["keySignature"]

        # Call your Python function passing selected_key
        # Replace the placeholders with the actual results

        major_scale = "C, D, E, F, G, A, B"
        major_chord = "C, E, G"
        minor_chord = "C, D#, G"

        return render_template(
            "index.html",
            key_signatures=key_signatures,
            selected_key=selected_key,
            major_scale=major_scale,
            major_chord=major_chord,
            minor_chord=minor_chord,
        )

    return render_template("index.html", key_signatures=key_signatures)


if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template, request
from notes import get_major_scale, get_key_signatures

app = Flask(__name__)

for x in pattern[y]:
    print(scale[x])
