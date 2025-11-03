from typing import Annotated
from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from application.core.connection import async_session


async def get_session():
    async with async_session.begin() as session:
        yield session


SessionDep = Annotated[AsyncSession, Depends(get_session)]
