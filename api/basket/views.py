from fastapi import APIRouter, Depends

from core.schemas.basket import BasketCreate
from crud.basket import get_basket_by_user
from crud.basket import get_baskets as baskets_get
from crud.basket import create_basket as basket_create


router = APIRouter(
    tags=["Basket"],
    prefix="/v1"
)


@router.post("/create_basket")
async def creat_basket(
        basket_in: BasketCreate
):
    basket = await basket_create(basket_in=basket_in)
    return basket


@router.get("/all_baskets{id}")
async def get_products(user_id: int):
    basket = await get_basket_by_user(user_id=user_id)
    return basket


@router.get("/all_baskets")
async def get_baskets():
    baskets = await baskets_get()
    return baskets
