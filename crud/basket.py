from sqlalchemy import select

from core.db_helper import db_helper
from core.models import Product
from core.models.basket import Basket
from core.schemas.basket import BasketCreate, BasketRead


async def create_basket(basket_in: BasketCreate) -> BasketRead:
    async with db_helper.session_factory() as session:
        new_basket = Basket(
            user_id=basket_in.user_id,
            product_id=basket_in.product_id,
            all_price=basket_in.all_price
        )
        session.add(new_basket)
        await session.commit()
    # await session.refresh(product)
    return new_basket


async def get_basket_by_user(user_id: int):
    async with db_helper.session_factory() as session:
        query = select(Basket.__table__.columns).where(Basket.user_id == user_id)
        result = await session.execute(query)
        return result.mappings().all()


async def get_baskets():
    async with db_helper.session_factory() as session:
        query = select(Basket.__table__.columns)
        result = await session.execute(query)
        return result.mappings().all()
