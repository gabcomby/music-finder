from read_music_file import readWavFile
from fourier_transform import performFourierTransform
from hashing import generate_music_hashes
import pickle
from typing import Dict, List, Tuple

def addMusicToDatabase(musicPath):
    try:
        database = pickle.load(open("database.pickle", "rb"))
    except FileNotFoundError:
        database: Dict[int, List[Tuple[int, int]]] = {}
    
    try:
        songIndex = pickle.load(open("song_index.pickle", "rb"))
    except FileNotFoundError:
        songIndex = {}

    # 1. Read WAV file and extract the audio data (mono) and sampling frequency
    samplingFreq, musicData = readWavFile(musicPath)

    # 2. Perform Fourier Transform to get the music map
    music_map = performFourierTransform(musicData, samplingFreq)

    # 3. Generate music hashes from the music map
    # Returns a dictionary of hashes (hash -> (time, song_id))
    music_hashes = generate_music_hashes(music_map, len(songIndex))

    # 4. Append the name of the song to the list of song names
    musicName = musicPath.split("/")[-1]
    songIndex[len(songIndex)] = musicName

    # 5. Insert the (time, song_id) pairs to the database with the associated hash as key
    for hash, time_id_pair in music_hashes.items():
        if hash not in database:
            database[hash] = []
        database[hash].append(time_id_pair)
    
    pickle.dump(database, open("database.pickle", "wb"), pickle.HIGHEST_PROTOCOL)
    pickle.dump(songIndex, open("song_index.pickle", "wb"), pickle.HIGHEST_PROTOCOL)