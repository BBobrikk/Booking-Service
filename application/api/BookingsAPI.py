from fastapi import HTTPException
from application.schemas.bookingDto import BookingCreate, BookingRead
from application.utils.dependency import SessionDep
from application.services.booking_service import (
    check_booking,
    check_bookings,
    check_user_bookings,
    cancel_booking,
    book_room,
)
from fastapi import APIRouter


booking_router = APIRouter(prefix="/bookings", tags=["Bookings"])


@booking_router.get("", response_model=list[BookingRead])
async def bookings(session: SessionDep):
    try:
        result = await check_bookings(session)
        return result
    except ValueError as er:
        raise HTTPException(status_code=404, detail=str(er))


@booking_router.get("/{booking_id}", response_model=BookingRead)
async def booking(session: SessionDep, booking_id: int):
    try:
        result = await check_booking(session, booking_id)
        return result
    except ValueError as er:
        raise HTTPException(status_code=404, detail=str(er))


@booking_router.get("/{user_id}", response_model=list[BookingRead])
async def user_bookings(session: SessionDep, user_id: int):
    try:
        result = await check_user_bookings(session, user_id)
        return result
    except ValueError as er:
        raise HTTPException(status_code=404, detail=str(er))


@booking_router.post("")
async def add_booking(session: SessionDep, booking_data: BookingCreate):
    try:
        await book_room(session, booking_data)
        return {"status": "Номер забронирован"}
    except Exception as er:
        raise HTTPException(status_code=422, detail=str(er))


@booking_router.delete("/booking_id")
async def del_booking(session: SessionDep, booking_id: int):
    try:
        await cancel_booking(session, booking_id)
        return {"status": "Бронирование отменено"}
    except ValueError as er:
        raise HTTPException(status_code=404, detail=str(er))
