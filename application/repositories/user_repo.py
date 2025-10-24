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
    session.add(user)
    return user


async def get_user(session: AsyncSession, user_id: int):
    user = await session.get(UserBase, user_id)
    return user


async def del_user(session: AsyncSession, user_id):
    user = await get_user(session, user_id)
    await session.delete(user)


async def get_user_by_name(session: AsyncSession, user_name=str):
    query = select(UsersORM).filter(UsersORM.name == user_name)
    user = await session.execute(query)
    return user.scalars().all()
