from httpx import AsyncClient, ASGITransport
from application.main import app


class TestRooms:

    async def test_get_rooms(self):
        async with AsyncClient(
            transport=ASGITransport(app), base_url="http://test"
        ) as client:
            response = await client.get("/rooms")
            assert response.status_code == 200 and len(response.json()) == 3

    async def test_get_room(self):
        async with AsyncClient(
            transport=ASGITransport(app), base_url="http://test"
        ) as client:
            response = await client.get("/rooms/1")
            assert response.status_code == 200 and response.json()[0]["number"] == 1

    async def test_available_rooms(self):
        pass

    async def test_grade_rooms(self):
        async with AsyncClient(
            transport=ASGITransport(app), base_url="http://test"
        ) as client:
            response = await client.get("/rooms/grade/standard")
            assert (
                response.status_code == 200
                and response.json()[0]["grade"] == "standard"
            )

    async def test_add_room(self):
        async with AsyncClient(
            transport=ASGITransport(app), base_url="http://test"
        ) as client:
            room = {"number": 4, "grade": "luxe", "beds": 2}
            await client.post("/rooms/create", json=room)
            response = await client.get("/rooms")
            assert response.status_code == 200 and len(response.json()) == 4

    async def test_del_room(self):
        async with AsyncClient(
            transport=ASGITransport(app), base_url="http://test"
        ) as client:
            await client.delete("/rooms/remove", params={"room_id": 1})
            response = await client.get("/rooms")
            assert response.status_code == 200 and len(response.json()) == 2
