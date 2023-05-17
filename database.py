from motor.motor_asyncio import AsyncIOMotorClient
from bson.objectid import ObjectId
from pymongo import ASCENDING, DESCENDING

# initialize MongoDB client
mongo_client = AsyncIOMotorClient("mongodb://localhost:27017")
db = mongo_client["bookstore_db"]
collection = db["books"]

# indexes to optimize query performance and prevent duplicate entries into the database
collection.create_index([("title", ASCENDING), ("author", ASCENDING)], unique=True)
collection.create_index([("title", ASCENDING)])
collection.create_index([("author", ASCENDING)])
collection.create_index([("price", ASCENDING)])

books_sold = {}

# a helper function to parse the given data into a dictionary
def book_helper(book) -> dict:
    return {
        "id": str(book["_id"]),
        "title": book["title"],
        "author": book["author"],
        "description": book["description"],
        "price": book["price"],
        "stock": book["stock"]
    }

def convert_to_title(book_data):
    # loop through the values in book_data and convert all text 
    # into lowercase
    for k, v in book_data.items():
        if type(v) == str:
            book_data[k] = v.title()
    return book_data

# function to retrieve all books stored in the database
async def retrieve_all_books():
    books = []
    # loop through the entire collection and append each document 
    # to the books list
    async for book in collection.find():
        books.append(book_helper(book))
    return books

# function to retrieve a single book by their ID number
async def retrieve_book(id: str) -> dict:
    book = await collection.find_one({"_id": ObjectId(id)})
    if book:
        return book_helper(book)

# function to add a new book to the database
async def add_book(book_data: dict) -> dict:
    book_data = convert_to_title(book_data)

    book = await collection.insert_one(book_data)
    new_book = await collection.find_one({"_id": book.inserted_id})
    return book_helper(new_book)
    
# function to update the data of a book given their ID
async def update_book(id: str, data: dict):
    # if no data was given, return false
    if len(data) < 1:
        return False

    data = convert_to_title(data)
    
    # find the book with the given ID
    book = await collection.find_one({"_id": ObjectId(id)})
    # if the book exists, then update its data with the new information
    # if the book was updated, return true
    # otherwise, return false
    if book:
        updated_book = await collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_book:
            return True
        return False
    
# function to delete a book from the database by their ID
async def delete_book(id: str):
    # find the book from the collection
    book = await collection.find_one({"_id": ObjectId(id)})
    # if the book exists, return true
    if book:
        await collection.delete_one({"_id": ObjectId(id)})
        return True

# function to retrieve books with the given title
async def retrieve_book_by_title(title: str) -> dict:
    books = []
    # loop through the collection and add all books that match the 
    # given title to the books list
    async for book in collection.find({"title": {"$eq": title.title()}}):
        books.append(book_helper(book))
    return books

# function to retrieve books with the given author
async def retrieve_book_by_author(author: str) -> dict:
    books = []
    # loop through the collection and add all books that match the 
    # given author to the books list
    async for book in collection.find({"author": {"$eq": author.title()}}):
        books.append(book_helper(book))
    return books

# function to retrieve books with the given price range
async def retrieve_book_by_price(lower_bound_price: float, upper_bound_price: float) -> dict:
    books = []
    # loop through the collection and add all books that match the 
    # given price range to the books list
    async for book in collection.find({"$and": [{"price": {"$gte": float(lower_bound_price)}}, {"price": {"$lte": float(upper_bound_price)}}]}):
        books.append(book_helper(book))
        print(books)
    return books

# function to update the data of a book given their ID
async def purchase_book(id: str, amount: int):
    # if the amount to be purchased is negative, return false
    if int(amount) < 0:
        return False
    
    # find the book with the given ID
    book = await collection.find_one({"_id": ObjectId(id)})

    # if the amount to be purchased is more than the amount in stock, return false
    if book['stock'] < amount:
        return False
    
    if book:
        # decrease the amount of books in stock with the given ID
        new_stock_amount = book['stock'] - amount
        # update the book stock in the database to the new amount after the purchase
        updated_book = await collection.update_one({"_id": ObjectId(id)}, {"$set": {"stock": new_stock_amount}})
        # if the stock has been updated, add the book ID and amount purchased to the list books_sold
        if updated_book:
            books_sold[id] = books_sold.get(id, 0) + amount
            return True
        return False

# function to retrieve the total number of books in the store
async def retrieve_total_num_books():
    return

# function to retrieve the top 5 bestselling books in the store
async def retrieve_topfive_bestselling():
    return

# function to retrieve the top 5 bestselling authors in the store
async def retrieve_topfive_authors():
    return