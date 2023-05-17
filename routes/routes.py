from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from database import (
    add_book,
    delete_book,
    retrieve_all_books,
    retrieve_book,
    update_book,
)

from models import (
    ErrorResponseModel,
    ResponseModel,
    BookSchema,
    UpdateBookModel
)

router = APIRouter()

@router.get("/", response_description="All Books retrieved!")
async def get_all_books():
    books = await retrieve_all_books()
    if books:
        return ResponseModel(books, "All books retrieved successfully!")
    return ResponseModel(books, "Empty list returned.")

@router.get("/{id}", response_description="Book retrieved!")
async def get_book_by_id(id):
    book = await retrieve_book(id)
    if book:
        return ResponseModel(book, "Book retrieved successfully!")
    return ErrorResponseModel("An error occurred.", 404, "Book doesn't exist.")

@router.post("/", response_description="New book added into the database")
async def add_new_book(book: BookSchema = Body(...)):
    book = jsonable_encoder(book)
    new_book = await add_book(book)
    return ResponseModel(new_book, "Book added successfully!")

@router.put("/id")
async def update_book_by_id(id: str, req: UpdateBookModel = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_book = await update_book(id, req)
    if updated_book:
        return ResponseModel(
            "Book with ID: {} update is successful!".format(id),
            "Book was updated successfully!"
        )
    return ErrorResponseModel(
        "An error occurred", 404, "Book with id {0} doesn't exist.".format(id)
    )

@router.delete("/id", response_description="Book was deleted from the database")
async def delete_book_by_id(id: str):
    deleted_book = await delete_book(id)
    if deleted_book:
        return ResponseModel(
            "Book with ID: {} removed".format(id),
            "Book deleted successfully!"
        )
    return ErrorResponseModel(
        "An error occurred", 404, "Book with id {0} doesn't exist.".format(id)
    )