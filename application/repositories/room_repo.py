from datetime import date
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from application.core.connection import async_session
from application.models.bookings import BookingsORM
from application.models.rooms import RoomsORM
from application.schemas.bookingDto import BookingCreate
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


async def get_available_rooms(session: AsyncSession, booking_data: BookingCreate):
    query = (
        select(RoomsORM)
        .join(BookingsORM.room_id, RoomsORM.room_id)
        .filter(booking_data.end > BookingsORM.start)
    )
    bookings = await session.execute(query)
    return bookings.scalars().all()


async def del_room(session: AsyncSession, room_id):
    room = await get_room(session, room_id)
    await session.delete(room)
