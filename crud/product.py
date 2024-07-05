from typing import Dict

from sqlalchemy import select, update

from core.db_helper import db_helper
from core.models import Product
from core.schemas.product import (ProductCreate,
                                  ProductRead,
                                  ProductUpdatePartial
                                  )


async def create_product(product_in: ProductCreate) -> Product:
    async with db_helper.session_factory() as session:
        new_product = Product(
            name=product_in.name,
            description=product_in.description,
            price=product_in.price
        )
        session.add(new_product)
        await session.commit()
    # await session.refresh(product)
    return new_product


async def get_product(product_id: int) -> ProductRead | None:
    async with db_helper.session_factory() as session:
        product = await session.get(Product, product_id)
        return product


async def get_products() -> list[Product]:
    async with db_helper.session_factory() as session:
        query = select(Product).order_by(Product.id)
        result = await session.execute(query)
        product = result.scalars().all()
        return list(product)


async def update_product(
        product_id: int,
        product_up: ProductUpdatePartial,
) -> Dict:
    async with db_helper.session_factory() as session:
        query = (
            update(Product)
            .where(Product.id == product_id)
            .values(name=product_up.name,
                    description=product_up.description,
                    price=product_up.price
                    )
            .execution_options(synchronize_session="fetch")
        )
        up_product = await session.execute(query)
        await session.commit()
        return {"success": True}
