from pydub import AudioSegment
from pydub.playback import play
import wave
from time import sleep
import simpleaudio as sa


test1 = "C"
test2 = "D"
test3 = "E"
test4 = "F"
test5 = "G"
test6 = "A"
test7 = "B"

string1 = "./media/{}.wav".format(test1)
string2 = "./media/{}.wav".format(test2)
string3 = "./media/{}.wav".format(test3)
string4 = "./media/{}.wav".format(test4)
string5 = "./media/{}.wav".format(test5)
string6 = "./media/{}.wav".format(test6)
string7 = "./media/{}.wav".format(test7)


audio1 = AudioSegment.from_file(string1)
audio2 = AudioSegment.from_file(string2)
audio3 = AudioSegment.from_file(string3)
audio4 = AudioSegment.from_file(string4)
audio5 = AudioSegment.from_file(string5)
audio6 = AudioSegment.from_file(string6)
audio7 = AudioSegment.from_file(string7)
# mixed = audio1.overlay(audio2).overlay(audio3).overlay(audio4)


# mixed.export("./created/mixed.wav", format="wav")
# string = "./created/mixed.wav"
play(audio1)
play(audio2)
play(audio3)
play(audio4)

# filename = "created/mixed.wav"
# wave_obj = sa.WaveObject.from_wave_file(filename)
# play_obj = wave_obj.play()
# play_obj.wait_done

# filename1 = "./media/{}.wav".format("A")
# filename2 = "./media/{}.wav".format("C")
# filename3 = "./media/{}.wav".format("E")

# wave_obj = sa.WaveObject.from_wave_file(filename)
# wave_obj = sa.WaveObject.from_wave_file(filename2)
# wave_obj = sa.WaveObject.from_wave_file(filename3)
# play_obj = wave_obj.play()
# play_obj.wait_done

# import wave

# sound1 = wave.open("/path/to/sound1", "rb")
# sound2 = wave.open("/path/to/sound2", "rb")


# def callback(in_data, frame_count, time_info, status):
#     data1 = sound1.readframes(frame_count)
#     data2 = sound2.readframes(frame_count)
#     decodeddata1 = numpy.fromstring(data1, numpy.int16)
#     decodeddata2 = numpy.fromstring(data2, numpy.int16)
#     newdata = (decodeddata1 * 0.5 + decodeddata2 * 0.5).astype(numpy.int16)
#     return (newdata.tostring(), pyaudio.paContinue)
