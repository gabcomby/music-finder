import pickle

import scipy as sp
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware

from database import addMusicToDatabase, findMusicInDatabase

app = FastAPI()

origins = ["http://localhost:5173", "http://localhost"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/test")
def test_endpoint():
    return {"message": "API is working"}


@app.post("/search")
def search_music(file: UploadFile = File(...)):
    songIndex = pickle.load(open("song_index.pickle", "rb"))
    file_data = file.file.read()
    matches = findMusicInDatabase(file_data)
    results = {songIndex[song_id]: score for song_id, score in matches}
    file.file.close()
    return results


@app.post("/addSong")
def add_song(file: UploadFile = File(...)):
    file_data = file.file.read()
    sp.io.wavfile.write("temp.wav", 44100, sp.frombuffer(file_data, dtype=sp.int16))
    addMusicToDatabase("temp.wav")
    file.file.close()
    return {"message": "Song added successfully"}
