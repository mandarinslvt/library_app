# from sqlalchemy import d
from datetime import date, timedelta

BOOKS_DATA = [
    {
        "title": "Мастер и Маргарита",
        "author": "Михаил Булгаков",
        "isbn": "978-5-17-080085-8",
        "year": 1937,
        "genre": "Роман",
        "available_copies": 3,
    }, #1

    {
        "title": "Преступление и наказание",
        "author": "Фёдор Достоевский",
        "isbn": "978-5-389-06254-2",
        "year": 1866,
        "genre": "Классика",
        "available_copies": 2,
    }, #2

    {
        "title": "1984",
        "author": "Джордж Оруэлл",
        "isbn": "978-5-17-092523-0",
        "year": 1949,
        "genre": "Антиутопия",
        "available_copies": 5,
    }, #3

    {
        "title": "Мартин Иден",
        "author": "Джек Лондон",
        "isbn": "979-5-19-193623-0",
        "year": 1908,
        "genre": "проза",
        "available_copies": 6,
    }, #4

    {
        "title": "А зори здесь тихие..",
        "author": "Борис Васильев",
        "isbn": "979-5-20-473623-3",
        "year": 1969,
        "genre": "Повесть",
        "available_copies": 2,
    }, #5

    {
        "title": "Жизнь на продажу",
        "author": "Юкио Мисима",
        "isbn": "978-4-30-577663-0",
        "year": 1968,
        "genre": "Роман",
        "available_copies": 4,
    }, #6

    {
        "title": "Палата № 6",
        "author": "Антон Чехов",
        "isbn": "979-2-17-894123-1",
        "year": 1892,
        "genre": "Сатира",
        "available_copies": 2,
    }, #7
]

READERS_DATA = [
    {
        "full_name": "Иван Иванов",
        "email": "ivan@example.com",
        "phone": "+79991112233",
        "registration_date": date.today() - timedelta(days=30),
    }, #1

    {
        "full_name": "Анна Петрова",
        "email": "anna@example.com",
        "phone": "+79992223344",
        "registration_date": date.today() - timedelta(days=15),
    }, #2

    {
        "full_name": "Пётр Котеков",
        "email": "petro22@example.com",
        "phone": "+79991168282",
        "registration_date": date.today() - timedelta(days=20),
    }, #3

    {
        "full_name": "Джон Васильев",
        "email": "vasyavasya@example.com",
        "phone": "+79892903456",
        "registration_date": date.today() - timedelta(days=11),
    }, #4

    {
        "full_name": "Абдулла Абдуллаев",
        "email": "abdullavv@example.com",
        "phone": "+79346771213",
        "registration_date": date.today() - timedelta(days=40),
    }, #5
]

USERS_DATA = [
    {
        "username": "admin",
        "email": "admin@library.ru",
        "password": "admin123",
        "role": "admin",
    },

    {
        "username": "librarian1",
        "email": "lib1@library.ru",
        "password": "lib12345",
        "role": "librarian",
    },
    
    {
        "username": "librarian2",
        "email": "lib2@library.ru",
        "password": "lib67890",
        "role": "librarian",
    },
]

HISTORY_DATA = [
    {
        "reader_id": 1,
        "book_id": 1,
        "taken_date": date.today() - timedelta(days=10),
        "return_at": date.today() - timedelta(days=3),
    },

    {
        "reader_id": 2,
        "book_id": 3,
        "taken_date": date.today() - timedelta(days=5),
        "return_at": None, 
    },

    {
        "reader_id": 3,
        "book_id": 2,
        "taken_date": date.today() - timedelta(days=25),
        "return_at": date.today() - timedelta(days=6), 
    },

    {
        "reader_id": 4,
        "book_id": 3,
        "taken_date": date.today() - timedelta(days=7),
        "return_at": None,  
    },
    {
        "reader_id": 5,
        "book_id": 5,
        "taken_date": date.today() - timedelta(days=20),
        "return_at": date.today() - timedelta(days=4)
    },
]