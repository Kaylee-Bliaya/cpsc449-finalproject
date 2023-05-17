from fastapi import FastAPI
from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError
from routes import router as BookRouter

app = FastAPI()

app.include_router(BookRouter, tags=["Book"], prefix="/books")

@app.get('/', tags=["Root"])
async def index():
    return {"message": "Welcome to this Bookstore API!"}