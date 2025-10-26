from datetime import date

from fastapi import APIRouter, HTTPException
from application.schemas.roomDto import RoomRead, RoomBase
from application.services.room_service import check_rooms, check_room, check_grade_rooms, create_room, remove_room, check_available_room
from application.utils.dependency import SessionDep


room_router = APIRouter(prefix="/rooms", tags=["Rooms"])

@room_router.get("", response_model=list[RoomRead])
async def rooms(session : SessionDep):
    try:
        result = await check_rooms(session)
        return result
    except ValueError as er:
        raise HTTPException(status_code=404, detail=str(er))

@room_router.get("/{room_number}", response_model=list[RoomRead])
async def room(session : SessionDep, room_number : int):
    try:
        result = await check_room(session, room_number)
        return result
    except ValueError as er:
        raise HTTPException(status_code=404, detail=str(er))

@room_router.get("/available/{booking_start}", response_model=list[RoomRead])
async def available_rooms(session : SessionDep, booking_start : date):
    try:
        result = await check_available_room(session, booking_start)
        return result
    except ValueError as er:
            raise HTTPException(status_code=404, detail=str(er))

@room_router.get("/grade/{grade}", response_model=list[RoomRead])
async def grade_rooms(session : SessionDep, grade : str):
    try:
        result = await check_grade_rooms(session, grade)
        return result
    except ValueError as er:
        raise HTTPException(status_code=404, detail=str(er))

@room_router.post("/create")
async def add_room(session : SessionDep, room_data : RoomBase):
    try:
        await create_room(session, room_data)
        return {"status" : "Номер создан"}
    except ValueError as er:
        raise HTTPException(status_code=422, detail=str(er))

@room_router.delete("/remove")
async def del_room(session : SessionDep, room_id : int):
    try:
        await remove_room(session, room_id)
        return {"status" : "Номер удалён"}
    except ValueError as er:
        raise HTTPException(status_code=404, detail=str(er))