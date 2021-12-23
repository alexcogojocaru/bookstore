from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from playhouse.shortcuts import model_to_dict
from db_models import *
from models import *

import json

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

class BooksAPI:
    @app.get('/api/bookcollection/books')
    async def get_books(page: int=0, items_per_page: int=5, genre: str=None, year: int=None):
        conditions = None
        if genre and year:
            conditions = BookDB.genre == genre and BookDB.year == year

        if not(genre and year):
            conditions = BookDB.genre == genre if genre else (BookDB.year == year if year else None)
        return list(model_to_dict(book) for book in BookDB.select().where(conditions))[page * items_per_page:(page + 1) * items_per_page]

    @app.get('/api/bookcollection/books/{isbn}')
    async def get_book_by_isbn(isbn: str):
        try:
            book = BookDB.get(BookDB.isbn == isbn)
            return model_to_dict(book)
        except:
            raise HTTPException(status.HTTP_404_NOT_FOUND, 'Book doesn\'t exist')

    @app.post('/api/bookcollection/books/{isbn}')
    async def update_book(isbn: str, book: Book):
        try:
            bookdb = BookDB.get(BookDB.isbn == isbn)
            bookdb.title        = book.title
            bookdb.publisher    = book.publisher
            bookdb.year         = book.year
            bookdb.genre        = book.genre
            bookdb.save()

            return model_to_dict(bookdb)
        except:
            raise HttpException(status.HTTP_404_NOT_FOUND)

    @app.put('/api/bookcollection/books')
    async def add_book(book: Book):
        book = BookDB.create(isbn=book.isbn, title=book.title, publisher=book.publisher, year=book.year, genre=book.genre)
        return model_to_dict(book)

    @app.delete('/api/bookcollection/books/{isbn}')
    async def delete_book(isbn: str):
        try:
            book = BookDB.get(BookDB.isbn == isbn)
            book.delete_instance()
        except:
            raise HttpException(status.HTTP_404_NOT_FOUND)

class AuthorsAPI:
    @app.get('/api/bookcollection/authors')
    async def get_authors(name: str=None, match: str=None):
        conditions = None
        if name and (match == 'exact'):
            conditions = AuthorDB.firstname == name
        elif name:
            conditions = AuthorDB.firstname.contains(name)
        return list(model_to_dict(author) for author in AuthorDB.select().where(conditions))

    @app.get('/api/bookcollection/authors/{id}')
    async def get_author_by_id(id: str):
        try:
            author = AuthorDB.get(AuthorDB.id == id)
            return model_to_dict(author)
        except:
            raise HTTPException(status.HTTP_404_NOT_FOUND, 'Author doesn\'t exist')

    @app.put('/api/bookcollection/authors')
    async def add_author(author: Author):
        author = AuthorDB.create(firstname=author.firstname, lastname=author.lastname)
        return model_to_dict(author)

    @app.post('/api/bookcollection/authors/{id}')
    async def update_author(id: str, author: Author):
        try:
            authordb = AuthorDB.get(AuthorDB.id == id)
            authordb.firstname  = author.firstname
            authordb.lastname   = author.lastname
            authordb.save()

            return model_to_dict(authordb)
        except:
            raise HttpException(status.HTTP_404_NOT_FOUND)
    
    @app.delete('/api/bookcollection/authors/{id}')
    async def delete_book(id: str):
        try:
            author = AuthorDB.get(AuthorDB.id == id)
            author.delete_instance()
        except:
            raise HttpException(status.HTTP_404_NOT_FOUND)

class BooksAuthorsAPI:
    @app.get('/api/bookcollection/books/{isbn}/authors')
    async def get_book_authors(isbn: str):
        try:
            book = BookDB.get(BookDB.isbn == isbn)
            data = BooksAuthorsDB.get(BooksAuthorsDB.book == book)

            return model_to_dict(data.author)
        except:
            raise HttpException(status.HTTP_404_NOT_FOUND)