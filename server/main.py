from database import addMusicToDatabase, findMusicInDatabase
import scipy as sp
import pickle


def main():
    songIndex = pickle.load(open("song_index.pickle", "rb"))
    addMusicToDatabase("./data/Fred Again - Victory Lap Five.wav")
    matches = findMusicInDatabase(
        "./data/test1.wav")
    for song_id, score in matches:
        print(f"{songIndex[song_id]}: Score of {score[1]} at {score[0]}")


if __name__ == "__main__":
    main()
