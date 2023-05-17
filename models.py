from typing import Optional
from pydantic import BaseModel, Field

# schema to represent how the book data will be stored in the database
class BookSchema(BaseModel):
    title: str = Field(...)
    author: str = Field(...)
    description: str = Field(...)
    price: float = Field(..., gt=0)
    stock: int = Field(..., ge=0)

    class Config:
        schema_extra = {
            "example": {
                "title": "Ex Book Title",
                "author": "Ex Author",
                "description": "Ex book description",
                "price": 1.00,
                "stock": 1
            }
        }

# schema to represent how the book data will be stored in the database 
# when updating values
class UpdateBookModel(BaseModel):
    title: Optional[str]
    author: Optional[str]
    description: Optional[str]
    price: Optional[float]
    stock: Optional[int]

    class Config:
        schema_extra = {
            "example": {
                "title": "Ex Updated Book Title",
                "author": "Ex Updated Author",
                "description": "Ex Updated book description",
                "price": 2.00,
                "stock": 2
            }
        }

# a response model to return when an API endpoint has successfully ran
def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message
    }

# a response model to return when an API endpoint has failed to run
def ErrorResponseModel(error, code, message):
    return {
        "error": error,
        "code": code,
        "message": message
    }