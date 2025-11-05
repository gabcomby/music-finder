from fourier_transform import performFourierTransform
from hashing import generate_music_hashes
import scipy as sp

def main():
    # 1. Read WAV file and extract the audio data (mono) and sampling frequency
    samplingFreq, musicData = readWavFile("data/Love Again (GARABATTO Remix) - Dua Lipa.wav")

    # 2. Perform Fourier Transform to get the music map
    music_map = performFourierTransform(musicData, samplingFreq)

    # 3. Generate music hashes from the music map
    music_hashes = generate_music_hashes(music_map, 0)
    for i, (hash, (time, _)) in enumerate(music_hashes.items()):
        if i > 10: 
            break
        print(f"Hash {hash} occurred at {time}")

def readWavFile(filepath):
    samplingFreq, musicData = sp.io.wavfile.read(filepath)
    # If stereo, take only one channel
    if musicData.ndim > 1:
        musicData = musicData[:, 0]
    return samplingFreq, musicData

if __name__ == "__main__":
    main()
