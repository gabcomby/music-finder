import scipy as sp


def readWavFile(filepath):
    samplingFreq, musicData = sp.io.wavfile.read(filepath)
    # If stereo, take only one channel
    if musicData.ndim > 1:
        musicData = musicData[:, 0]
    return samplingFreq, musicData
