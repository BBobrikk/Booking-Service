from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from application.core.connection import async_session
from application.models.users import UsersORM
from application.schemas.userDto import UserBase


async def get_all_users(session: AsyncSession):
    query = select(UsersORM)
    query = await session.execute(query)
    return query.scalars().all()


async def add_user(session: AsyncSession, user_data: UserBase):
    user = UsersORM(name=user_data.name, phone=user_data.phone, mail=user_data.mail)
    return user


async def get_users(session: AsyncSession, room_id: int):
    user = await session.get(UserBase, room_id)
    return user
