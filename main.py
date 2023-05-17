from fastapi import FastAPI
from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError
from routes.routes import router as BookRouter
from routes.search_title_route import router as SearchByTitleRouter
from routes.search_author_route import router as SearchByAuthorRouter
from routes.search_price_route import router as SearchByPriceRouter
from routes.purchase_route import router as PurchaseRouter

from database import (retrieve_total_num_books, retrieve_topfive_authors, retrieve_topfive_bestselling)

app = FastAPI()

# connection to the routes
app.include_router(BookRouter, tags=["Book"], prefix="/books")
app.include_router(SearchByTitleRouter, tags=["Search"], prefix="/search_by_title")
app.include_router(SearchByAuthorRouter, tags=["Search"], prefix="/search_by_author")
app.include_router(SearchByPriceRouter, tags=["Search"], prefix="/search_by_price")
app.include_router(PurchaseRouter, tags=["Purchase Book(s)"], prefix="/purchase")

@app.get('/', tags=["Root"])
async def index():
    await retrieve_topfive_bestselling()
    await retrieve_topfive_authors()
    return {"message": "Welcome to this Bookstore API!"}

@app.get('/books_in_stock', tags=["Root"])
async def get_total_books():
    total_books = await retrieve_total_num_books()
    return {"Total Books in Stock": total_books}

@app.get('/topselling_books', tags=["Root"])
async def get_topselling_books():
    books = await retrieve_topfive_bestselling()
    return {"Top 5 Bestselling Books:": books}

@app.get('/topselling_authors', tags=["Root"])
async def get_topselling_authors():
    authors = await retrieve_topfive_authors()
    return {"Top 5 Bestselling Authors": authors}