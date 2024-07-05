import asyncio
import json
import sys

import pytest
from httpx import AsyncClient, ASGITransport
from sqlalchemy import insert

from core.config import settings
from core.db_helper import db_helper
from core.models import Base, User, Product, Basket
from main import main_app

if sys.platform == "win32":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


@pytest.fixture(scope="session", autouse=True)
async def prepare_database():
    assert settings.MODE == "TEST"
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

    def open_mock_json(model: str):
        with open(f"tests/mock_{model}.json", "r") as file:
            return json.load(file)

    user = open_mock_json("users")
    product = open_mock_json("products")
    basket = open_mock_json("baskets")

    async with db_helper.session_factory() as session:
        add_user = insert(User).values(user)
        add_product = insert(Product).values(product)
        add_basket = insert(Basket).values(basket)
        await session.execute(add_user)
        await session.execute(add_product)
        await session.execute(add_basket)
        await session.commit()


# @pytest.fixture(scope="session")
# def event_loop_policy():
#     policy = asyncio.WindowsSelectorEventLoopPolicy()
#     asyncio.set_event_loop_policy(policy)
#     return policy
@pytest.fixture(scope="session")
def event_loop(request):
    """Create an instance of the default event loop for each test case."""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="function")
async def ac():
    async with AsyncClient(transport=ASGITransport(app=main_app), base_url="http://test") as ac:
        yield ac
