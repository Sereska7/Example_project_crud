from fastapi import APIRouter

from core.schemas.user import UserRead, UserUpdatePartial
from crud.user import get_user as user_get
from crud.user import get_users as users_get
from crud.user import update_user as user_update

router = APIRouter(
    tags=["Users"],
    prefix="/v1"
)


@router.get("/user/{id}")
async def get_user(user_id: int) -> UserRead:
    return await user_get(user_id=user_id)


@router.get("/all_users")
async def get_users() -> list[UserRead]:
    users = await users_get()
    return list(users)


@router.patch("/update_user{id}")
async def update_user(
        user_id: int,
        user_up: UserUpdatePartial,
):
    return await user_update(user_id, user_up)
