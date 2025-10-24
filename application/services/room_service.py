from sqlalchemy.ext.asyncio import AsyncSession
from application.repositories.room_repo import (
    del_room,
    get_available_rooms,
    get_room,
    add_room,
    get_all_rooms,
)


async def check_rooms(session: AsyncSession):
    rooms = await get_all_rooms(session)
    if rooms:
        return rooms
    raise ValueError("Номера не найдены")
