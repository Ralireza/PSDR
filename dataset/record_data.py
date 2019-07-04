import sounddevice as sd
from scipy.io.wavfile import write
import os

def record_voice():
    # create folders
    for i in range(10):
        if not os.path.exists(str(i)):
            os.mkdir(str(i))

    fs = 8000
    seconds = 2

    name = input("Please Enter Your Name:")
    label= input("Please Enter Your Label:")

    for i in range(10):
        input("Please press Enter to record voice {}_{}_{}:".format(label,name, i))
        my_recording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
        sd.wait()
        write('{}/{}_{}_{}.wav'.format(label,label,name,i), fs, my_recording)


record_voice()


