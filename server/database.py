import io
import pickle
from typing import Dict, List, Tuple

import scipy as sp

from fourier_transform import performFourierTransform
from hashing import generate_music_hashes


# Not yet updated to work with direct file
def addMusicToDatabase(file_data):
    try:
        database = pickle.load(open("database.pickle", "rb"))
    except FileNotFoundError:
        database: Dict[int, List[Tuple[int, int]]] = {}

    try:
        songIndex = pickle.load(open("song_index.pickle", "rb"))
    except FileNotFoundError:
        songIndex = {}

    # 1. Read WAV file and extract the audio data (mono) and sampling frequency
    samplingFreq, musicData = sp.io.wavfile.read(io.BytesIO(file_data))

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


# Updated to work with direct file
def findMusicInDatabase(file_data):
    database = pickle.load(open("database.pickle", "rb"))

    # 1. Read WAV file and extract the audio data (mono) and sampling frequency
    samplingFreq, musicData = sp.io.wavfile.read(io.BytesIO(file_data))

    # 2. Perform Fourier Transform to get the music map
    music_map = performFourierTransform(musicData, samplingFreq)

    # 3. Generate music hashes from the music map
    # Returns a dictionary of hashes (hash -> (time, song_id))
    music_hashes = generate_music_hashes(music_map, None)

    matches_per_song = {}
    for hash, (sample_time, _) in music_hashes.items():
        if hash in database:
            matching_occurences = database[hash]
            for source_time, song_index in matching_occurences:
                if song_index not in matches_per_song:
                    matches_per_song[song_index] = []
                matches_per_song[song_index].append((hash, sample_time, source_time))

    # %%
    scores = {}
    for song_index, matches in matches_per_song.items():
        song_scores_by_offset = {}
        for hash, sample_time, source_time in matches:
            delta = source_time - sample_time
            if delta not in song_scores_by_offset:
                song_scores_by_offset[delta] = 0
            song_scores_by_offset[delta] += 1

        max = (0, 0)
        for offset, score in song_scores_by_offset.items():
            if score > max[1]:
                max = (offset, score)

        scores[song_index] = max

    # Sort the scores for the user
    scores = list(sorted(scores.items(), key=lambda x: x[1][1], reverse=True))

    # Return the top scoring song
    return scores[0]
