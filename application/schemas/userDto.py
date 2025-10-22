from pydantic import BaseModel


class UserBase(BaseModel):
    name: str
    phone: str
    mail: str


class UserRead(UserBase):
    room_id: int
