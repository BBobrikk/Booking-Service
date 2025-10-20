from pydantic import BaseModel
from DataBase.Parameters import *


class Settings(BaseModel):

    host: str
    port: str
    user: str
    db: str
    password: str

    def ASYNC_ENGINE_CREATE(self):
        return f"postgresql+asyncpg://{self.user}:{self.password}@{self.host}:{self.port}/{self.db}"


settings = Settings(host=host, port=port, user=user, db=db, password=password)
