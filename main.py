from database import addMusicToDatabase, findMusicInDatabase
import scipy as sp
import pickle

def main():
    songIndex = pickle.load(open("song_index.pickle", "rb"))
    # addMusicToDatabase("data/Daft Punk - Television Rules The Nation.wav")
    matches = findMusicInDatabase("./data/MY OLD WAYS - (MORGAN PAGE BOOTLEG MIX) - Morgan Page.wav")
    for song_id, score in matches:
        print(f"{songIndex[song_id]}: Score of {score[1]} at {score[0]}")

if __name__ == "__main__":
    main()
