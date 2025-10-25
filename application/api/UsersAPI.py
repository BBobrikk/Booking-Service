from fastapi import HTTPException
from application.utils.dependency import SessionDep
from application.services.user_service import check_users
from fastapi import APIRouter
from uvicorn import run

user_router = APIRouter(prefix = "/users", tags=["Users"])

@user_router.get("/")
async def users(session : SessionDep):
    try:
        await check_users(session)
    except Exception as er:
        raise HTTPException(status_code=404, detail=str(er))

if __name__ == "__main__":
    run("application:main:app", reload = True)