import pickle

import scipy as sp
from fastapi import FastAPI, File, HTTPException, UploadFile
from fastapi.middleware.cors import CORSMiddleware

from database import addMusicToDatabase, findMusicInDatabase

SONG_MATCH_THRESHOLD = 50

app = FastAPI()

origins = ["http://localhost:5173", "http://localhost"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/search")
def search_music(file: UploadFile = File(...)):
    songIndex = pickle.load(open("song_index.pickle", "rb"))
    file_data = file.file.read()
    song_id, (offset, score) = findMusicInDatabase(file_data)
    file.file.close()
    if (score) > SONG_MATCH_THRESHOLD:
        return {
            "song_name": songIndex[song_id],
            "offset": offset,
            "score": score,
        }
    else:
        raise HTTPException(status_code=404, detail="No satisfying match found in DB")
    # results = {songIndex[song_id]: score for song_id, score in matches}


@app.post("/addSong")
def add_song(file: UploadFile = File(...)):
    file_data = file.file.read()
    sp.io.wavfile.write("temp.wav", 44100, sp.frombuffer(file_data, dtype=sp.int16))
    addMusicToDatabase("temp.wav")
    file.file.close()
    return {"message": "Song added successfully"}
