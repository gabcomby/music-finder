import scipy as sp
from scipy import signal
import numpy as np

def main():
    samplingFreq, musicData = readWavFile("data/Love Again (GARABATTO Remix) - Dua Lipa.wav")
    performFourierTransform(samplingFreq, musicData)

def performFourierTransform(samplingFreq, musicData):
    window_length_seconds = 0.5
    window_length_samples = int(window_length_seconds * samplingFreq)
    window_length_samples += window_length_samples % 2
    num_peaks = 15

    padding = window_length_samples - musicData.size % window_length_samples
    paddedMusicData = np.pad(musicData, (0, padding))

    frequencies, times, stft = signal.stft(paddedMusicData, samplingFreq, nperseg=window_length_samples, nfft=window_length_samples, return_onesided=True)

    music_map = []

    for time_index, window in range(stft.T):
        spectrum = np.abs(window)
        peaks, props = signal.find_peaks(spectrum, prominence=0, distance=200)
        n_peaks = min(num_peaks, len(peaks))
        largest_peaks = np.argpartition(props["prominences"], -n_peaks)[-n_peaks:]
        for peak in peaks[largest_peaks]:
            frequency = frequencies[peak]
            music_map.append([time_index, frequency])

    return music_map

def readWavFile(filepath):
    samplingFreq, musicData = sp.io.wavfile.read(filepath)
    return samplingFreq, musicData

if __name__ == "__main__":
    main()
