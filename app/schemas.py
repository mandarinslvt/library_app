from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime

class BookModel(BaseModel):
    point_id: int
    point_author: str
    point_title: str

class BookDetail(BookModel):
    available_status: bool
    reader_name: str | None

class ReaderModel(BaseModel):
    point_id: int
    point_name: str

class ReaderProfile(ReaderModel):
    reading_history: list[BookModel]

class UserBase(BaseModel):
    full_name: str
    email: EmailStr
    role: str = "librarian"

class UserCreate(UserBase):
    password: str = Field(..., min_length=6)

class UserUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None
    role: Optional[str] = None
    is_active: Optional[bool] = None

class UserResponse(UserBase):
    id: int
    is_active: bool
    created_at: datetime
    reader_id: Optional[int] = None

class Config:
    from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None
    role: Optional[str] = None

class LoginRequest(BaseModel):
    username: str
    password: str