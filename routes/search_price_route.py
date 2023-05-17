from fastapi import APIRouter

from database import retrieve_book_by_price

from models import ResponseModel

router = APIRouter()

@router.get("/{price}", response_description="Book retrieved by price range!")
async def search_book_by_price(lower_bound_price, upper_bound_price):
    books = await retrieve_book_by_price(lower_bound_price, upper_bound_price)
    if books:
        return ResponseModel(books, "Book retrieved successfully!")
    return ResponseModel(books, "Empty list returned.")