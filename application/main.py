import asyncio
from application.core.connection import async_engine
from application.core.connection import Base


async def setup():
    async with async_engine.begin() as connect:
        await connect.run_sync(Base.metadata.drop_all)
        await connect.run_sync(Base.metadata.create_all)


async def main():
    await setup()


if __name__ == "__main__":
    asyncio.run(main())
