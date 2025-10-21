from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase
from application.core.Configuration import settings

async_engine = create_async_engine(settings.ASYNC_ENGINE_CREATE())

async_session = async_sessionmaker(async_engine)


class Base(DeclarativeBase):
    pass
