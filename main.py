from contextlib import asynccontextmanager
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend

from redis import asyncio as aioredis

import uvicorn
from fastapi import FastAPI
from api.user import user_router
from api.product import router_products
from api.auth import router_auth
from api.basket import router_basket
from core.db_helper import db_helper


@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup
    redis = aioredis.from_url("redis://localhost:6379/0")
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")
    yield
    # shutdown
    await db_helper.dispose()


main_app = FastAPI(lifespan=lifespan)


main_app.include_router(user_router)
main_app.include_router(router_products)
main_app.include_router(router_auth)
main_app.include_router(router_basket)


if __name__ == "__main__":
    uvicorn.run("main:main_app", reload=True)
