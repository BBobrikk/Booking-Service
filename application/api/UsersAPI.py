from fastapi import HTTPException
from application.schemas.userDto import UserRead, UserBase
from application.utils.dependency import SessionDep
from application.services.user_service import (
    check_users,
    registration_user,
    find_user,
    remove_user,
)
from fastapi import APIRouter

user_router = APIRouter(prefix="/users", tags=["Users"])


@user_router.get("", response_model=list[UserRead])
async def users(session: SessionDep):
    try:
        result = await check_users(session)
        return result
    except ValueError as er:
        raise HTTPException(status_code=404, detail=str(er))


@user_router.get("/{username}", response_model=list[UserRead])
async def user(session: SessionDep, username: str):
    try:
        result = await find_user(session, username)
        return result
    except ValueError as er:
        raise HTTPException(status_code=404, detail=str(er))


@user_router.post("")
async def add_user(session: SessionDep, user_data: UserBase):
    try:
        await registration_user(session, user_data)
        return {"status": "Пользователь успешно создан"}
    except ValueError as er:
        raise HTTPException(status_code=422, detail=str(er))


@user_router.delete("user_id")
async def delete_user(session: SessionDep, user_id: int):
    try:
        await remove_user(session, user_id)
        return {"status": "Пользователь удалён"}
    except Exception as er:
        raise HTTPException(status_code=404, detail=str(er))
