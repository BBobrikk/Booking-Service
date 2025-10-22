from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from application.core.connection import async_session
from application.models.bookings import BookingsORM
from application.schemas.bookingDto import BookingCreate


async def get_all_bookings(session: AsyncSession):
    query = select(BookingsORM)
    query = await session.execute(query)
    return query.scalars().all()


async def add_booking(session: AsyncSession, booking_data: BookingCreate):
    booking = BookingsORM(
        user_id=booking_data.user_id,
        room_id=booking_data.room_id,
        price=booking_data.price,
        code=booking_data.code,
        start=booking_data.start,
        end=booking_data.end,
        wishes=booking_data.wishes,
    )
    return booking


async def get_booking(session: AsyncSession, room_id: int):
    booking = await session.get(BookingsORM, room_id)
    return booking
