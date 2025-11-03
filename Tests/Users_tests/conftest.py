import pytest
from application.core.connection import async_session
from application.models import UsersORM
from application.utils.database_setup import setup_db


users = [
    UsersORM(name="Arthur Morgan", phone="+77777777777", mail="test1@mail.ru"),
    UsersORM(name="John Marston", phone="+78888888888", mail="test2@gmail.com"),
    UsersORM(name="Alex Mercer", phone="+70000000000", mail="test3@mail.ru"),
]


@pytest.fixture(autouse=True)
async def setup_environment():
    await setup_db()

    async with async_session.begin() as session:
        session.add_all(users)

    yield
