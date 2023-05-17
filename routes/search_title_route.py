from fastapi import APIRouter
from database import retrieve_book_by_title
from models import ResponseModel

router = APIRouter()

# an API endpoint to get a book with the given title
@router.get("/{title}", response_description="Book retrieved by title!")
async def search_book_by_title(title):
    books = await retrieve_book_by_title(title)
    if books:
        return ResponseModel(books, "Book retrieved successfully!")
    return ResponseModel(books, f"There are no books with the title '{title.title()}' in stock.")