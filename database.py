from motor.motor_asyncio import AsyncIOMotorClient
from bson.objectid import ObjectId
from pymongo import ASCENDING, DESCENDING

# Initialize MongoDB client
mongo_client = AsyncIOMotorClient("mongodb://localhost:27017")
db = mongo_client["bookstore_db"]
collection = db["books"]

collection.create_index([("title", ASCENDING)])
collection.create_index([("author", ASCENDING)])
collection.create_index([("price", ASCENDING)])

def book_helper(book) -> dict:
    return {
        "id": str(book["_id"]),
        "title": book["title"],
        "author": book["author"],
        "description": book["description"],
        "price": book["price"],
        "stock": book["stock"]
    }

async def retrieve_all_books():
    books = []
    async for book in collection.find():
        books.append(book_helper(book))
    return books

async def retrieve_book(id: str) -> dict:
    book = await collection.find_one({"_id": ObjectId(id)})
    if book:
        return book_helper(book)

async def add_book(book_data: dict) -> dict:
    book = await collection.insert_one(book_data)
    new_book = await collection.find_one({"_id": book.inserted_id})
    return book_helper(new_book)
    
async def update_book(id: str, data: dict):
    if len(data) < 1:
        return False
    
    book = await collection.find_one({"_id": ObjectId(id)})
    if book:
        updated_book = await collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_book:
            return True
        return False
    
async def delete_book(id: str):
    book = await collection.find_one({"_id": ObjectId(id)})
    if book:
        await collection.delete_one({"_id": ObjectId(id)})
        return True
    
async def retrieve_total_num_books():
    return

async def retrieve_topfive_bestselling():
    return

async def retrieve_topfive_authors():
    return

async def retrieve_topfive_authors():
    return

async def retrieve_book_by_title(title: str) -> dict:
    books = []
    async for book in collection.find({"title": {"$eq": title.upper()}}):
        books.append(book_helper(book))
    return books

async def retrieve_book_by_author(author: str) -> dict:
    books = []
    async for book in collection.find({"author": {"$eq": author}}):
        books.append(book_helper(book))
    return books

async def retrieve_book_by_price(lower_bound_price: float, upper_bound_price: float) -> dict:
    books = []
    async for book in collection.find({"$and": [{"price": {"$gte": float(lower_bound_price)}}, {"price": {"$lte": float(upper_bound_price)}}]}):
        books.append(book_helper(book))
        print(books)
    return books