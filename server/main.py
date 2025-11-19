from database import addMusicToDatabase, findMusicInDatabase
import scipy as sp
import pickle
from fastapi import FastAPI, File, UploadFile

app = FastAPI()


@app.get("/search")
def search_music(file: UploadFile = File(...)):
    songIndex = pickle.load(open("song_index.pickle", "rb"))
    file_data = file.file.read()
    sp.io.wavfile.write("temp.wav", 44100, sp.frombuffer(
        file_data, dtype=sp.int16))
    matches = findMusicInDatabase("temp.wav")
    results = {songIndex[song_id]: score for song_id, score in matches}
    file.file.close()
    return results


@app.post("/addSong")
def add_song(file: UploadFile = File(...)):
    file_data = file.file.read()
    sp.io.wavfile.write("temp.wav", 44100, sp.frombuffer(
        file_data, dtype=sp.int16))
    addMusicToDatabase("temp.wav")
    file.file.close()
    return {"message": "Song added successfully"}
