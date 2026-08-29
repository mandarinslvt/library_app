from datetime import date
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Date, ForeignKey

class Base(DeclarativeBase):
    pass

class Book(Base):
    __tablename__ = 'books'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String, nullable=False)
    author: Mapped[str] = mapped_column(String, nullable=False)
    isbn: Mapped[str] = mapped_column(String, nullable=True)
    year: Mapped[int] = mapped_column(Integer, nullable=True)
    genre: Mapped[str] = mapped_column(String, nullable=True)
    available_copies: Mapped[int] = mapped_column(Integer, default=1)

class Reader(Base):
    __tablename__ = 'readers'
    id: Mapped[int] = mapped_column (Integer, primary_key=True)
    full_name: Mapped[str] = mapped_column (String, nullable=False)
    email: Mapped[str] = mapped_column (String, unique=True, nullable=False)
    phone: Mapped[str] = mapped_column (String, nullable=True)
    registration_date: Mapped[date] = mapped_column (Date, default=date.today)

class ReaderBooks(Base):
     __tablename__ = 'reader_book'
     id: Mapped[int] = mapped_column (Integer, primary_key=True)
     reader_id: Mapped[int] = mapped_column(ForeignKey("readers.id", ondelete="CASCADE"))
     book_id: Mapped[int] = mapped_column(ForeignKey("books.id", ondelete="CASCADE"))
     taken_date: Mapped[date] = mapped_column(Date, default=date.today)
     return_at: Mapped[date | None] = mapped_column(Date, nullable=True)