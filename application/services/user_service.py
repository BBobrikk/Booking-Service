from sqlalchemy.ext.asyncio import AsyncSession
from application.repositories.user_repo import (
    get_user,
    add_user,
    get_all_users,
    del_user,
    get_user_by_name,
)

from application.schemas.userDto import UserBase


async def registration_user(session: AsyncSession, user_data: UserBase):
    exciting_user = await get_user_by_name(session, user_data.name)
    if exciting_user:
        raise ValueError("Пользователь с этим именем существует")
    await add_user(session, user_data)


async def find_user(session: AsyncSession, username : str):
    user = await get_user_by_name(session, username)
    if user:
        return user
    raise ValueError("Пользователь не найден")


async def check_users(session: AsyncSession):
    users = await get_all_users(session)
    if users:
        return users
    raise ValueError("Пользователи не найдены")


async def remove_user(session: AsyncSession, user_id: int):
    user = await get_user(session, user_id)
    if user:
        await del_user(session, user_id)
    raise ValueError("Пользователь не найден")


