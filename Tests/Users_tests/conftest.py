import pytest
from application.core.connection import async_engine, async_session, Base
from application.models import  UsersORM

users = [UsersORM(name="Arthur Morgan", phone="+77777777777", mail="test1@mail.ru"),
         UsersORM(name="John Marston", phone="+78888888888", mail="test2@gmail.com"),
         UsersORM(name="Alex Mercer", phone="+70000000000", mail="test3@mail.ru")]


@pytest.fixture(autouse=True)
async def setup_environment():
    async with async_engine.begin() as connection:
        await connection.run_sync(Base.metadata.drop_all)
        await connection.run_sync(Base.metadata.create_all)


    async with async_session.begin() as session:
        session.add_all(users)

    yield
