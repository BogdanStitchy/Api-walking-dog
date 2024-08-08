import pytest
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from httpx import AsyncClient, ASGITransport

from app.main import app as public_media_app
from config import config
from app.db.base_model import engine, Base, async_session_maker


@pytest.fixture(scope="session", autouse=True)
def check_mode():
    if config.MODE != "TEST":
        pytest.exit(f"Прерывание тестовой серии: MODE!=TEST\nMODE={config.MODE}")


@pytest.fixture(scope="session", autouse=True)
async def prepare_database():
    assert config.MODE == "TEST"

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


@pytest.fixture(scope="function")
async def async_client():
    async with AsyncClient(transport=ASGITransport(app=public_media_app), base_url="http://test") as ac:
        yield ac


@pytest.fixture(scope="function")
async def clear_db_table_order():
    async with async_session_maker() as session:
        memes_table = Base.metadata.tables['orders']
        await session.execute(memes_table.delete())
        await session.commit()
        print("Table orders was clear")


@pytest.fixture(scope="module")
async def start_redis_for_method_with_cache():
    FastAPICache.init(RedisBackend("redis://localhost"), prefix="fastapi-cache")
