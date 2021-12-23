from db_models import *
import json

books = json.load(open('books.json', 'r'))
authors = { item['author']: [item['author'].split(' ')[0], item['author'].split(' ')[1]] for item in books }
authors = { name: AuthorDB.create(firstname=authors[name][0], lastname=authors[name][1]) for name in authors.keys() }

for item in books:
    book = BookDB.create(isbn=item['isbn'], title=item['title'], publisher=item['publisher'], year=item['year_published'], genre=item['genre'], stock=10)
    author = authors[item['author']]

    BooksAuthorsDB.create(book=book, author=author)
