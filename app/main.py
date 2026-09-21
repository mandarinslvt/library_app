from fastapi import FastAPI, Depends, HTTPException, status
from app.schemas import BookModel, BookDetail, ReaderModel, ReaderProfile
from app.database import SessionLocal
from app.models import User
from app.schemas import Token
from app.auth import verify_password, create_access_token
import jwt
from jwt.exceptions import InvalidTokenError as JWTError
from app.auth import auth_router 

app = FastAPI() 

app.include_router(auth_router)
app = FastAPI() 
@app.get('/')
def read_root():
    return {'Message': 'HELLO WORLD!'}


@app.get('/books')
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