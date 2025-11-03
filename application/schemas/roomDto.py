from pydantic import BaseModel


class RoomBase(BaseModel):
    number: int
    grade: str
    beds: int

    class Config:
        from_attributes = True


class RoomRead(RoomBase):
    room_id: int

    class Config:
        from_attributes = True
