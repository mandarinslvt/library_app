from database import engine, SessionLocal
from models import Base, Book, Reader, ReaderBooks, User
from auth import get_password_hash 
from data import BOOKS_DATA, READERS_DATA, HISTORY_DATA, USERS_DATA

Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)
with SessionLocal() as db:
    for book_dict in BOOKS_DATA:
        db.add(Book(**book_dict))
        
    for reader_dict in READERS_DATA:
        db.add(Reader(**reader_dict))
    db.commit()  

    for history_dict in HISTORY_DATA:
        db.add(ReaderBooks(**history_dict))
    db.commit()

    for user_dict in USERS_DATA:
        user_data = user_dict.copy()
        plain_password = user_data.pop("password")
        user_data["password_hash"] = get_password_hash(plain_password)
        db.add(User(**user_dict))
    db.commit()

    print("База данных успешно пересоздана и заполнена!")