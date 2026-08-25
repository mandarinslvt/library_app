from pydantic import BaseModel

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
