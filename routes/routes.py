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

# an API endpoint to get all books in the database
@router.get("/", response_description="All Books retrieved!")
async def get_all_books():
    books = await retrieve_all_books()
    if books:
        return ResponseModel(books, "All books were successfully retrieved!")
    return ResponseModel(books, "There are no books in stock.")

# an API endpoint to get a book with the given ID
@router.get("/{id}", response_description="Book retrieved!")
async def get_book_by_id(id):
    book = await retrieve_book(id)
    if book:
        return ResponseModel(book, f"The book with ID [{id}] was ssuccessfully retrieved!")
    return ErrorResponseModel("An error occurred.", 404, f"The book with the ID {id} doesn't exist.")

# an API endpoint to add a new book into the database
@router.post("/", response_description="New book added into the database.")
async def add_new_book(book: BookSchema = Body(...)):
    book = jsonable_encoder(book)
    try:
        new_book = await add_book(book)
    except:
        return ErrorResponseModel(
            "An error occurred", 404, 
            f"The book '{book['title'].title()}' by {book['author'].title()} already exists in the database."
        )
    return ResponseModel(new_book, "The book was successfully added to the database!")

# an API endpoint to update a book with the given ID
@router.put("/id")
async def update_book_by_id(id: str, req: UpdateBookModel = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_book = await update_book(id, req)
    if updated_book:
        return ResponseModel(
            f"The book with ID [{id}] was successfully updated!",
            "Book was updated successfully!"
        )
    return ErrorResponseModel(
        "An error occurred", 404, f"The book with ID [{id}] doesn't exist."
    )

# an API endpoint to delete a book with the given ID
@router.delete("/id", response_description="Book was deleted from the database")
async def delete_book_by_id(id: str):
    deleted_book = await delete_book(id)
    if deleted_book:
        return ResponseModel(
            f"The book with ID [{id}] was successfully removed!",
            "Book deleted successfully!"
        )
    return ErrorResponseModel(
        "An error occurred", 404, f"The book with ID [{id}] doesn't exist."
    )