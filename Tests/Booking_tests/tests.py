from datetime import date
from httpx import ASGITransport, AsyncClient
from application.main import app


class TestBookings:

    async def test_get_bookings(self):
        async with AsyncClient(
            transport=ASGITransport(app), base_url="http://test"
        ) as client:
            response = await client.get("/bookings")
            assert response.status_code == 200 and len(response.json()) == 3

    async def test_get_booking(self):
        async with AsyncClient(
            transport=ASGITransport(app), base_url="http://test"
        ) as client:
            response = await client.get("/bookings/1")
            assert response.status_code == 200 and response.json()["code"] == "code1"

    async def test_user_bookings(self):
        async with AsyncClient(
            transport=ASGITransport(app), base_url="http://test"
        ) as client:
            response = await client.get("/bookings/user/1")
            assert response.status_code == 200 and response.json()[0]["code"] == "code1"

    async def test_add_booking(self):
        async with AsyncClient(
            transport=ASGITransport(app), base_url="http://test"
        ) as client:
            booking = {
                "code": "code4",
                "price": 3300,
                "wishes": "wish4",
                "start_date": date(year=2025, month=11, day=10).isoformat(),
                "end_date": date(year=2025, month=11, day=13).isoformat(),
                "user_id": 1,
                "room_id": 1,
            }
            await client.post("/bookings/create", json=booking)
            response = await client.get("/bookings")
            assert response.status_code == 200 and len(response.json()) == 4

    async def test_del_booking(self):
        async with AsyncClient(
            transport=ASGITransport(app), base_url="http://test"
        ) as client:
            await client.delete("/bookings/remove", params={"booking_id": 1})
            response = await client.get("/bookings")
            assert response.status_code == 200 and len(response.json()) == 2
