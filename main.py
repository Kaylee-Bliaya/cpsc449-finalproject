from fastapi import FastAPI
from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError
from routes.routes import router as BookRouter
from routes.search_title_route import router as SearchByTitleRouter
from routes.search_author_route import router as SearchByAuthorRouter
from routes.search_price_route import router as SearchByPriceRouter

app = FastAPI()

# connection to the routes
app.include_router(BookRouter, tags=["Book"], prefix="/books")
app.include_router(SearchByTitleRouter, tags=["Search Books by Title"], prefix="/search_by_title")
app.include_router(SearchByAuthorRouter, tags=["Search Books by Author"], prefix="/search_by_author")
app.include_router(SearchByPriceRouter, tags=["Search Books by Price"], prefix="/search_by_price")

@app.get('/', tags=["Root"])
async def index():
    return {"message": "Welcome to this Bookstore API!"}