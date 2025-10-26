from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from application.models import BookingsORM
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
        start_date=booking_data.start_date,
        end_date=booking_data.end_date,
        wishes=booking_data.wishes,
    )
    session.add(booking)


async def get_booking_by_code(session: AsyncSession, booking_code: str):
    query = select(BookingsORM).filter(BookingsORM.code == booking_code)
    result = await session.execute(query)
    return result.scalars().all()

async def get_booking(session : AsyncSession, booking_id : int):
    booking = await session.get(BookingsORM, booking_id)
    return booking

async def delete_booking(session: AsyncSession, booking_id: int):
    booking = await get_booking(session, booking_id)
    await session.delete(booking)


async def get_user_bookings(session: AsyncSession, user_id: int):
    query = select(BookingsORM).filter(BookingsORM.user_id == user_id)
    bookings = await session.execute(query)
    return bookings.scalars().all()
