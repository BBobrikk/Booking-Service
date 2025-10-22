from pydantic import BaseModel


class RoomBase(BaseModel):
    number: int
    grade: str
    beds: int


class RoomRead(RoomBase):
    room_id: int
