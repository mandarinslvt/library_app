from fastapi import FastAPI
from app.schemas import BookModel, BookDetail, ReaderModel, ReaderProfile

app = FastAPI() 

@app.get('/')
def read_root():
    return {'Message': 'HELLO WORLD!'}

@app.get('/books', response_model = list[BookModel])
def books_list():
    return {'bookTitles': []}


@app.get('/readers', response_model = list[ReaderModel])
def readers_list():
    return {'Readers': []}


@app.get('/readers/{reader_id}', response_model = ReaderProfile)
def readers_id(reader_id: int):
    return {'reader_id': reader_id, 'history': []}


@app.get('/books/{books_id}', response_model = BookModel)
def books_id(books_id: int):
    return {'books_id': books_id, 'details': {}}
