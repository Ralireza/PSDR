import sounddevice as sd
from scipy.io.wavfile import write
import os

def record_voice():
    fs = 8000
    seconds = 2
    name = input("Please Enter Your Name:")
    label= input("Please Enter Your Label:")
    os.mkdir(name)
    for i in range(10):
        input("Please press Enter to record voice {}_{}_{}:".format(label,name, i))
        myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
        sd.wait()
        write('{}/{}_{}_{}.wav'.format(name,label,name,i), fs, myrecording)


record_voice()


