from pydub import AudioSegment
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


# # userinput = "C"
# # chordselect = aug7th


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
