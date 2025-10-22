from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    host: str
    port: str
    user: str
    db: str
    password: str

    model_config = SettingsConfigDict(env_file=".env")

    def ASYNC_ENGINE_CREATE(self):
        return f"postgresql+asyncpg://{self.user}:{self.password}@{self.host}:{self.port}/{self.db}"


settings = Settings()
