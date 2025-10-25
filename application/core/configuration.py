from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path


BASE_DIR = Path(__file__).parent.parent.parent


class Settings(BaseSettings):

    host: str
    port: str
    user: str
    db: str
    password: str

    model_config = SettingsConfigDict(
        env_file=BASE_DIR / ".env",
        env_file_encoding="utf-8")

    def ASYNC_ENGINE_CREATE(self):
        return f"postgresql+asyncpg://{self.user}:{self.password}@{self.host}:{self.port}/{self.db}"


settings = Settings()
