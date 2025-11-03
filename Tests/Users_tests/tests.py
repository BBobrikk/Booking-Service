from httpx import AsyncClient, ASGITransport
from application.main import app


class TestUsers:

    async def test_get_users(self):
        async with AsyncClient(
            transport=ASGITransport(app), base_url="http://test"
        ) as client:
            response = await client.get("/users")
            assert response.status_code == 200 and len(response.json()) == 3

    async def test_get_user(self):
        async with AsyncClient(
            transport=ASGITransport(app), base_url="http://test"
        ) as client:
            response = await client.get("/users/Arthur Morgan")
            assert (
                response.status_code == 200
                and response.json()[0]["name"] == "Arthur Morgan"
            )

    async def test_add_user(self):
        async with AsyncClient(
            transport=ASGITransport(app), base_url="http://test"
        ) as client:
            user = {"name": "John Snow", "phone": "88888888888", "mail": "test4mail.ru"}
            await client.post("/users/create", json=user)
            response = await client.get("/users")
            assert response.status_code == 200 and len(response.json()) == 4

    async def test_del_user(self):
        async with AsyncClient(
            transport=ASGITransport(app), base_url="http://test"
        ) as client:
            await client.delete("/users/delete", params={"user_id": 1})
            response = await client.get("/users")
            assert response.status_code == 200 and len(response.json()) == 2
