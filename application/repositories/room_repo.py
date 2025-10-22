from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from application.core.connection import async_session
from application.models.rooms import RoomsORM
from application.schemas.roomDto import RoomBase


async def get_all_rooms(session: AsyncSession):
    query = select(RoomsORM)
    query = await session.execute(query)
    return query.scalars().all()


async def add_room(session: AsyncSession, room_data: RoomBase):
    room = RoomsORM(number=room_data.number, grade=room_data.grade, beds=room_data.beds)
    return room


async def get_room(session: AsyncSession, room_id: int):
    room = await session.get(RoomsORM, room_id)
    return room
