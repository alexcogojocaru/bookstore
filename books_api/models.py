from pydantic import BaseModel


class Book(BaseModel):
    isbn: str
    title: str
    publisher: str
    year: int
    genre: str

class Author(BaseModel):
    firstname: str
    lastname: str
