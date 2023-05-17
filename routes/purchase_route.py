from fastapi import APIRouter
from database import purchase_book
from models import ErrorResponseModel, ResponseModel

router = APIRouter()

# an API endpoint to update a book with the given ID
@router.put("/id")
async def update_book_by_id(id: str, amount: int):
    updated_book = await purchase_book(id, amount)
    if updated_book:
        return ResponseModel(
            f"The book with ID [{id}] was successfully purchased!",
            "Book was purchased successfully!"
        )
    return ErrorResponseModel(
        "An error occurred", 404, f"The are not enough books with ID [{id}] in stock."
    )