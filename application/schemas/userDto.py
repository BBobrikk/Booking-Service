from pydantic import BaseModel


class UserBase(BaseModel):
    name: str
    phone: str
    mail: str

    class Config:
        from_attributes = True


class UserRead(UserBase):
    user_id: int

    class Config:
        from_attributes = True
