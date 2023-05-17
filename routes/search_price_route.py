from fastapi import APIRouter
from database import retrieve_book_by_price
from models import ResponseModel, ErrorResponseModel

router = APIRouter()

# an API endpoint to get a book with the given price range
@router.get("/{price}", response_description="Book retrieved by price range!")
async def search_book_by_price(lower_bound_price, upper_bound_price):
    # check to see if negative prices were given
    # if so, return an error response
    if float(lower_bound_price) < 0 or float(upper_bound_price) < 0:
        return ErrorResponseModel(
            "An error occurred", 404, f"Prices can't be a negative amount."
        )
    
    books = await retrieve_book_by_price(lower_bound_price, upper_bound_price)
    if books:
        return ResponseModel(books, "Book retrieved successfully!")
    
    # reformat the upper and lower price bounds as currency
    price1 = "${:,.2f}".format(float(lower_bound_price))
    price2 = "${:,.2f}".format(float(upper_bound_price))
    return ResponseModel(books, f"There are no books within the price range [{price1} - {price2}] in stock.")