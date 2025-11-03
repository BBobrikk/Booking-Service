from application.models import RoomsORM, UsersORM, BookingsORM
from application.core.connection import async_session
from application.utils.database_setup import setup_db
import pytest
from datetime import date


date(year=2025, month=11, day=5)
room = RoomsORM(number=1, grade="standard", beds=1)
user = UsersORM(name="Arthur Morgan", phone="+77777777777", mail="test1@mail.ru")
bookings = [
    BookingsORM(
        code="code1",
        price=2200,
        wishes="wish1",
        start_date=date(year=2025, month=11, day=3),
        end_date=date(year=2025, month=11, day=5),
        user_id=1,
        room_id=1,
    ),
    BookingsORM(
        code="code2",
        price=1500,
        wishes="wish2",
        start_date=date(year=2025, month=11, day=5),
        end_date=date(year=2025, month=11, day=8),
        user_id=1,
        room_id=1,
    ),
    BookingsORM(
        code="code3",
        price=3200,
        wishes="wish3",
        start_date=date(year=2025, month=11, day=8),
        end_date=date(year=2025, month=11, day=10),
        user_id=1,
        room_id=1,
    ),
]


@pytest.fixture(autouse=True)
async def setup_environment():

    await setup_db()

    async with async_session.begin() as session:
        session.add(room)
        session.add(user)
        session.add_all(bookings)

    yield
