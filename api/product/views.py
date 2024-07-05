from fastapi import APIRouter
from fastapi_cache.decorator import cache

from core.schemas.product import ProductCreate, ProductRead, ProductUpdatePartial
from crud.product import create_product as product_create
from crud.product import get_product as product_get
from crud.product import get_products as products_get
from crud.product import update_product as product_update

router = APIRouter(
    tags=["Products"],
    prefix="/v1"
)


@router.post("/crate_product")
async def create_product(
    product_in: ProductCreate,
):
    return await product_create(product_in=product_in)


@router.get("/product{id}")
@cache(expire=30)
async def get_product(product_id: int) -> ProductRead:
    product = await product_get(product_id=product_id)
    return product


@router.get("/all_products")
@cache(expire=30)
async def get_products():
    product = await products_get()
    return product


@router.patch("/update_product{id}")
async def update_product(
        product_id: int,
        product_up: ProductUpdatePartial,
):
    return await product_update(product_id, product_up)


# @router.get("/all_products")
# async def get_products(user: User = Depends(get_current_user)):
#     product = await products_get()
#     return product
