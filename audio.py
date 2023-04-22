from pydub import AudioSegment
import wave
from time import sleep
import simpleaudio as sa


# test1 = "B"
# test2 = "F#"
# test3 = "Db"
# test4 = "G"

# string1 = "./media/{}.wav".format(test1)
# string2 = "./media/{}.wav".format(test2)
# string3 = "./media/{}.wav".format(test3)
# string4 = "./media/{}.wav".format(test4)


# audio1 = AudioSegment.from_file(string1)
# audio2 = AudioSegment.from_file(string2)
# audio3 = AudioSegment.from_file(string3)
# audio4 = AudioSegment.from_file(string4)

# mixed = audio1.overlay(audio2).overlay(audio3).overlay(audio4)


# mixed.export("./created/mixed.wav", format="wav")
# string = "./created/mixed.wav"

filename = "created/mixed.wav"
wave_obj = sa.WaveObject.from_wave_file(filename)
play_obj = wave_obj.play()
play_obj.wait_done

# filename1 = "./media/{}.wav".format("A")
# filename2 = "./media/{}.wav".format("C")
# filename3 = "./media/{}.wav".format("E")

# wave_obj = sa.WaveObject.from_wave_file(filename)
# wave_obj = sa.WaveObject.from_wave_file(filename2)
# wave_obj = sa.WaveObject.from_wave_file(filename3)
# play_obj = wave_obj.play()
# play_obj.wait_done
