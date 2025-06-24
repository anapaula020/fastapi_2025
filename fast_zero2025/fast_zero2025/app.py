from fastapi import FastAPI
from fast_zero2025.app import app

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}