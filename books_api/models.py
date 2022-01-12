from peewee import Model
from peewee import CharField, TextField, IntegerField, ForeignKeyField
from peewee import MySQLDatabase

import os
import time

MARIADB_HOST = os.environ.get('MARIADB_HOST')
print(MARIADB_HOST)
maria_db = MySQLDatabase('bookstore', user='root', password='pass', host=MARIADB_HOST, port=3306)
is_connected = False

while not is_connected:
    try:
        maria_db.connect()
        is_connected = True
    except:
        pass
    print('Trying to connect to MariaDB Server', flush=True)
    time.sleep(2)

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