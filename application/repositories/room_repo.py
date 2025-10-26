from datetime import date

from sqlalchemy import select, and_
from sqlalchemy.ext.asyncio import AsyncSession
from application.models import BookingsORM
from application.models import RoomsORM
from application.schemas.roomDto import RoomBase


async def get_all_rooms(session: AsyncSession):
    query = select(RoomsORM)
    query = await session.execute(query)
    return query.scalars().all()


async def add_room(session: AsyncSession, room_data: RoomBase):
    room = RoomsORM(number=room_data.number, grade=room_data.grade, beds=room_data.beds)
    session.add(room)


async def get_room(session: AsyncSession, room_id: int):
    room = await session.get(RoomsORM, room_id)
    return room


async def get_available_rooms(session: AsyncSession, booking_date : date):
    query = (
        select(RoomsORM)
        .join(BookingsORM, BookingsORM.room_id == RoomsORM.room_id)
        .filter(booking_date > BookingsORM.end_date)
    )
    rooms = await session.execute(query)
    return rooms.scalars().all()

async def del_room(session: AsyncSession, room_id):
    room = await get_room(session, room_id)
    await session.delete(room)

async def get_room_by_grade(session : AsyncSession, grade : str):
    query = select(RoomsORM).filter(RoomsORM.grade == grade)
    rooms = await session.execute(query)
    return rooms.scalars().all()

async def get_room_by_number(session : AsyncSession, room_number : int):
    query = select(RoomsORM).filter(RoomsORM.number == room_number)
    room = await session.execute(query)
    return room.scalars().all()