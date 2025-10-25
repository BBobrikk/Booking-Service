from sqlalchemy.ext.asyncio import AsyncSession
from application.models import BookingsORM
from application.schemas.bookingDto import BookingCreate


from application.repositories.bookings_repo import (
    add_booking,
    get_user_bookings,
    delete_booking,
    get_booking,
    get_all_bookings
)
from application.repositories.room_repo import get_available_rooms


async def book_room(session: AsyncSession, booking_data: BookingCreate):
    available = await get_available_rooms(session, booking_data)
    if available:
        for room in available:
            if room.room_id == booking_data.room_id:
                await add_booking(session, booking_data)
    else:
        raise ValueError("Комната не доступна для бронирования")


async def cancel_booking(session: AsyncSession, booking_id: int):
    booking = await session.get(BookingsORM, booking_id)
    if booking:
        await delete_booking(session, booking_id)
    else:
        raise ValueError("Комната не забронирована")


async def check_user_bookings(session: AsyncSession, user_id: int):
    bookings = await get_user_bookings(session, user_id)
    if bookings:
        return bookings
    raise ValueError("Нет забронированных комнат")

async def check_bookings(session : AsyncSession):
    bookings = await get_all_bookings(session)
    if bookings:
        return bookings
    raise ValueError("Бронирования не найдены")

async def check_booking(session: AsyncSession, booking_id):
    booking = await get_booking(session, booking_id)
    if booking:
        return booking
    raise ValueError("Бронирование не найдено")