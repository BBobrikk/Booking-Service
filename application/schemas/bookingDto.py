from datetime import date
from pydantic import BaseModel


class BookingBase(BaseModel):
    code: str
    price: int
    wishes: list[str]
    start_date: date
    end_date: date


class BookingCreate(BookingBase):
    user_id: int
    room_id: int


class BookingRead(BookingCreate):
    booking_id: int
