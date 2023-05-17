from fastapi import APIRouter
from database import retrieve_book_by_author
from models import ResponseModel

router = APIRouter()

# an API endpoint to get a book with the given author
@router.get("/{author}", response_description="Book retrieved by author!")
async def search_book_by_author(author):
    books = await retrieve_book_by_author(author)
    if books:
        return ResponseModel(books, "Book retrieved successfully!")
    return ResponseModel(books, "Empty list returned.")