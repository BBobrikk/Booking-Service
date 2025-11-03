from application.models import RoomsORM
from application.core.connection import async_session
from application.utils.database_setup import setup_db
import pytest


rooms = [
    RoomsORM(number=1, grade="standard", beds=1),
    RoomsORM(number=2, grade="luxe", beds=2),
    RoomsORM(number=3, grade="president", beds=3),
]


@pytest.fixture(autouse=True)
async def setup_environment():

    await setup_db()

    async with async_session.begin() as session:
        session.add_all(rooms)

    yield
