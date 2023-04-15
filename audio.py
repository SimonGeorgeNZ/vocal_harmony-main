from pydub import AudioSegment
from playsound import playsound
from app import set_key

# test = harmonykeys("keynotes")

# print(test)


test1 = "A"
test2 = "C"
test3 = "D#"
test4 = "F"

string1 = "./media/{}.wav".format(test1)
string2 = "./media/{}.wav".format(test2)
string3 = "./media/{}.wav".format(test3)
string4 = "./media/{}.wav".format(test4)


audio1 = AudioSegment.from_file(string1)
audio2 = AudioSegment.from_file(string2)
audio3 = AudioSegment.from_file(string3)
audio4 = AudioSegment.from_file(string4)


mixed = audio1.overlay(audio2).overlay(audio3).overlay(audio4)

#     @classmethod
#     def from_wav(cls, file, parameters=None):
#         return cls.from_file(file, 'wav', parameters=parameters)

# class AudioSegment()
# @classmethod
# def from_file(cls, file, format=None, codec=None, parameters=None, start_second=None, duration=None, **kwargs):
#     orig_file = file


# test1 = "D"
# file = "./media/{}.wav".format(test1)
# # AS = AudioSegment()

# test = AudioSegment.from_file(file)
# print(test())


# print(file)

mixed.export("./created/mixed.wav", format="wav")  # export mixed  audio file

playsound("./created/mixed.wav")  # play mixed audio file
