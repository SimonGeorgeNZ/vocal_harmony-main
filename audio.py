from pydub import AudioSegment
from playsound import playsound

# test = harmonykeys("keynotes")

print(test)

# string = "./media/{}.wav".format(test)

# audio1 = AudioSegment.from_file("./media/E.wav")

# audio2 = AudioSegment.from_file("./media/F#.wav")
# audio3 = AudioSegment.from_file("./media/G#.wav")
# audio4 = AudioSegment.from_file("./media/C.wav")
# audio5 = AudioSegment.from_file("./media/A.wav")
# audio6 = AudioSegment.from_file("./media/Eb.wav")
# audio7 = AudioSegment.from_file("./media/B.wav")


# mixed = (
#     audio1.overlay(audio2)
#     .overlay(audio3)
#     .overlay(audio4)
#     .overlay(audio5)
#     .overlay(audio6)
#     .overlay(audio7)
# )

# @classmethod
#     def from_wav(cls, file, parameters=None):
#         return cls(AudioSegment ,'wav', parameters=parameters)
test = "C#"
file = "./media/{}.wav".format(test)
AS = AudioSegment

print(AS)

mixed.export("./created/mixed.wav", format="wav")  # export mixed  audio file

playsound("./created/mixed.wav")  # play mixed audio file
