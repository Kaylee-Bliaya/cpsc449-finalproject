from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from database import (
    add_book,
    delete_book,
    retrieve_all_books,
    retrieve_book,
    update_book,
    retrieve_total_num_books,
    retrieve_topfive_bestselling,
    retrieve_topfive_authors,
    retrieve_book_by_title,
    retrieve_book_by_author,
    retrieve_book_by_price
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
        return ResponseModel(books, "Books data retrieved successfully!")
    return ResponseModel(books, "Empty list returned.")

@router.get("/{id}", response_description="Book data retrieved!")
async def get_book_by_id(id):
    book = await retrieve_book(id)
    if book:
        return ResponseModel(book, "Book data retrieved successfully!")
    return ErrorResponseModel("An error occurred.", 404, "Book doesn't exitst.")

@router.post("/", response_description="Book data added into the database")
async def add_new_book(book: BookSchema = Body(...)):
    book = jsonable_encoder(book)
    new_book = await add_book(book)
    return ResponseModel(new_book, "Book added successfully!")

@router.put("/id")
async def update_book_by_id(id: str, req: UpdateBookModel = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    print(f"req: {req}")
    updated_book = await update_book(id, req)
    if updated_book:
        return ResponseModel(
            "Book with ID: {} update is successful!".format(id),
            "Book was updated successfully!"
        )
    return ErrorResponseModel(
        "An error occurred", 404, "Book with id {0} doesn't exist.".format(id)
    )

@router.delete("/id", response_description="Book data deleted from the database")
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

@router.get("/", response_description="Total number of books retrieved!")
async def get_total_books():
    return

@router.get("/", response_description="Top 5 bestselling books retrieved!")
async def get_topfive_bestselling():
    return

@router.get("/", response_description="Top 5 bestselling authors retrieved!")
async def get_topfive_authors():
    return

@router.get("/{title}", response_description="Book retrieved by title!")
async def get_book_by_title(title):
    return

@router.get("/{author}", response_description="Book retrieved by author!")
async def get_book_by_title(author):
    return

@router.get("/{price}", response_description="Book retrieved by price range!")
async def get_book_by_title(price):
    return