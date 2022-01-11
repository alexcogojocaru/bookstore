from peewee import Model
from peewee import CharField, TextField, IntegerField, ForeignKeyField
from peewee import MySQLDatabase


maria_db = MySQLDatabase('bookstore', user='root', password='pass', host='localhost', port=3306)
maria_db.connect()

class BaseModel(Model):
    class Meta:
        database = maria_db

class BookDB(BaseModel):
    isbn        = CharField(max_length=13, primary_key=True)
    title       = CharField(max_length=150, unique=True)
    publisher   = TextField()
    year        = IntegerField()
    genre       = CharField(max_length=20)
    stock       = IntegerField()

    class Meta:
        db_table = 'books'

class AuthorDB(BaseModel):
    firstname   = CharField(max_length=30)
    lastname    = CharField(max_length=30)

    class Meta:
        db_table = 'authors'
        indexes = (
            (('firstname', 'lastname'), True), 
        )

class BooksAuthorsDB(BaseModel):
    book    = ForeignKeyField(BookDB, backref='bookauthor', on_delete='CASCADE')
    author  = ForeignKeyField(AuthorDB, backref='bookauthor', on_delete='CASCADE')

    class Meta:
        db_table = 'booksauthors'

maria_db.create_tables([BookDB, AuthorDB, BooksAuthorsDB])