from fastapi import FastAPI

app = FastAPI() 
@app.get('/')
def read_root():
    return {'Message': 'HELLO WORLD!'}

@app.get('/books')
def books_list():
    return {'bookTitles': []}

@app.get('/readers')
def readers_list():
    return {'Readers': []}

@app.get('/readers/{reader_id}')
def readers_id(reader_id: int):
    return {'reader_id': reader_id, 'history': []}

@app.get('/books/{books_id}')
def books_id(books_id: int):
    return {'books_id': books_id, 'details': {}}