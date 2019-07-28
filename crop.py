import glob
from pydub import AudioSegment
import os


def detect_leading_silence(sound, silence_threshold=-55, chunk_size=10):
    '''
    sound is a pydub.AudioSegment
    silence_threshold in dB
    chunk_size in ms

    iterate over chunks until you find the first one with sound
    '''
    trim_ms = 0  # ms

    assert chunk_size > 0  # to avoid infinite loop
    while sound[trim_ms:trim_ms + chunk_size].dBFS < silence_threshold and trim_ms < len(sound):
        trim_ms += chunk_size

    return trim_ms


def removeSilence():
    proccessed_dataset = "dataset/"
    os.mkdir(proccessed_dataset)
    for i in range(10):
        os.mkdir(proccessed_dataset + str(i))

    for i in range(10):
        path = "dataset/{0}/*.*".format(i)
        j = 0
        for file in glob.glob(path):
            sound = AudioSegment.from_file(file, format="wav")

            start_trim = detect_leading_silence(sound)
            end_trim = detect_leading_silence(sound.reverse())

            duration = len(sound)
            trimmed_sound = sound[start_trim:duration - end_trim]

            trimmed_sound.export('dataset2/{0}/crop_sample{1}.wav'.format(i, j), format="wav")
            j += 1


removeSilence()
