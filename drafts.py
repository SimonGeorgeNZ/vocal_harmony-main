from pydub import AudioSegment
from pydub.playback import play

notes = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]

two2nd = [0, 2]
two4th = [0, 5]
two5th = [0, 7]
three3rd = [0, 4, 7]
threemin3 = [0, 3, 7]
three5th = [0, 7, 9]
diminished = [0, 3, 6]
dim7th = [0, 3, 6, 9]
halfdim = [0, 3, 6, 10]
augmented = [0, 4, 8]
aug7th = [0, 4, 8, 10]


newharm = []
userinput = "A"
chordselect = aug7th

counter = 0
root = userinput
# times = len(chordselect)
for i in notes:
    if root == i:
        start = notes.index(i)
        end = len(notes)
        notes = notes[start:end] + notes[0:start]
        for d in chordselect:
            each = notes[d]
            newharm.append(each)
            # print(newharm)
for a in newharm:
    counter = counter + 1
    Hstring = "media/{}.wav".format(a)
    # print(Hstring)
    if counter == 1:
        audio1 = AudioSegment.from_file(Hstring)
        print(counter)
        print(a)
        print(Hstring)
    if counter == 2:
        print(counter)
        print(a)
        print(Hstring)
        audio2 = AudioSegment.from_file(Hstring)
        out_f = audio1.overlay(audio2)
    if counter == 3:
        print(counter)
        print(a)
        print(Hstring)
        audio3 = AudioSegment.from_file(Hstring)
        out_f = out_f.overlay(audio3)
    if counter == 4:
        print(counter)
        print(a)
        print(Hstring)
        audio4 = AudioSegment.from_file(Hstring)
        out_f = out_f.overlay(audio4)
play(out_f)
