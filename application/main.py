from contextlib import asynccontextmanager
from fastapi import FastAPI
from uvicorn import run
from application.api.BookingsAPI import booking_router
from application.api.UsersAPI import user_router
from application.api.RoomsAPI import room_router
from application.utils.database_setup import setup_db


@asynccontextmanager
async def lifespan(app: FastAPI):

    await setup_db()

    yield


app = FastAPI(lifespan=lifespan)


app.include_router(user_router)
app.include_router(room_router)
app.include_router(booking_router)


if __name__ == "__main__":
    run("main:app", reload=True)
