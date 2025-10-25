from fastapi import FastAPI
from uvicorn import run
from asyncio import run as db_run
from application.api.UsersAPI import user_router
from application.core.connection import async_engine, Base

app = FastAPI()


app.include_router(user_router)

async def setup_db():
    async with async_engine.begin() as connect:
        await connect.run_sync(Base.metadata.drop_all)
        await connect.run_sync(Base.metadata.create_all)

if __name__ == "__main__":
    db_run(setup_db())
    run("main:app", reload=True)