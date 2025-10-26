from datetime import date
from sqlalchemy.ext.asyncio import AsyncSession
from application.repositories.room_repo import (
    del_room,
    get_available_rooms,
    get_room,
    add_room,
    get_all_rooms,
    get_room_by_grade,
    get_room_by_number
)
from application.schemas.roomDto import RoomBase


async def check_rooms(session: AsyncSession):
    rooms = await get_all_rooms(session)
    if rooms:
        return rooms
    raise ValueError("Номера не найдены")

async def check_available_room(session : AsyncSession, booking_data : date):
    rooms = await get_available_rooms(session, booking_data)
    if rooms:
        return rooms
    raise ValueError("Нет доступных номеров")

async def check_room(session : AsyncSession, room_number : int):
    room = await get_room_by_number(session, room_number)
    if room:
        return room
    raise ValueError("Номер не найден")

async def create_room(session : AsyncSession, room_data : RoomBase):
    room = await get_room_by_number(session, room_data.number)
    if room:
        raise ValueError("Номер уже существует")
    await add_room(session, room_data)

async def remove_room(session : AsyncSession, room_id : int):
    room = await get_room(session, room_id)
    if room:
        await del_room(session, room_id)
    else:
        raise ValueError("Номер не найден")

async def check_grade_rooms(session : AsyncSession, grade : str):
    rooms = await get_room_by_grade(session, grade)
    if rooms:
        return rooms
    raise ValueError("Номера не найдены")