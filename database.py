from motor.motor_asyncio import AsyncIOMotorClient
from bson.objectid import ObjectId

# Initialize MongoDB client
mongo_client = AsyncIOMotorClient("mongodb://localhost:27017")
db = mongo_client["bookstore_db"]
collection = db["books"]

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
    print(f"in update: {id}, {data}")
    if len(data) < 1:
        return False
    
    book = await collection.find_one({"_id": ObjectId(id)})
    print(f"book: {book}")
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
    return

async def retrieve_book_by_author(author: str) -> dict:
    return

async def retrieve_book_by_price(price: float) -> dict:
    return