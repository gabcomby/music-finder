from scipy import signal
import numpy as np

def performFourierTransform(musicData, samplingFreq):
    # Parameters
    window_length_seconds = 0.5
    window_length_samples = int(window_length_seconds * samplingFreq)
    window_length_samples += window_length_samples % 2
    num_peaks = 15

    # Pad the song to divide evenly into windows
    amount_to_pad = window_length_samples - musicData.size % window_length_samples
    song_input = np.pad(musicData, (0, amount_to_pad))

    # Perform a short time fourier transform
    frequencies, times, stft = signal.stft(
        song_input, samplingFreq, nperseg=window_length_samples, nfft=window_length_samples, return_onesided=True
    )
    constellation_map = []

    for time_idx, window in enumerate(stft.T):
        spectrum = abs(window)
        # Find peaks - these correspond to interesting features
        # Note the distance - want an even spread across the spectrum
        peaks, props = signal.find_peaks(spectrum, prominence=0, distance=200)

        # Only want the most prominent peaks
        # With a maximum of 15 per time slice
        n_peaks = min(num_peaks, len(peaks))
        # Get the n_peaks largest peaks from the prominences
        largest_peaks = np.argpartition(props["prominences"], -n_peaks)[-n_peaks:]
        for peak in peaks[largest_peaks]:
            frequency = frequencies[peak]
            constellation_map.append([time_idx, frequency])

    return constellation_map