from datetime import date
from pydantic import BaseModel


class BookingBase(BaseModel):
    code: str
    price: int
    wishes: str
    start_date: date
    end_date: date
    class Config:
        from_attributes = True


class BookingCreate(BookingBase):
    user_id: int
    room_id: int
    class Config:
        from_attributes = True


class BookingRead(BookingCreate):
    booking_id: int
    class Config:
        from_attributes = True

