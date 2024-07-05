from typing import Dict

from sqlalchemy import select, update

from core.auth.utils import get_password_hash
from core.db_helper import db_helper
from core.models import User
from core.schemas.user import (
    UserCreate,
    UserRead,
    UserUpdatePartial, UserReadLogin
)


async def create_user(user_in: UserCreate) -> UserRead:
    async with db_helper.session_factory() as session:
        new_user = User(
            email=user_in.email,
            password=get_password_hash(user_in.password))
        session.add(new_user)
        await session.commit()
    # await session.refresh(product)
    return new_user


async def get_user(user_id: int) -> UserRead | None:
    async with db_helper.session_factory() as session:
        user = await session.get(User, user_id)
        return user


async def get_users() -> list[UserRead]:
    async with db_helper.session_factory() as session:
        query = select(User).order_by(User.id)
        result = await session.execute(query)
        users = result.scalars().all()
        return list(users)


async def update_user(
        user_id: int,
        user_up: UserUpdatePartial,
) -> Dict:
    async with db_helper.session_factory() as session:
        query = (
            update(User)
            .where(User.id == user_id)
            .values(email=user_up.email, password=get_password_hash(user_up.password))
            .execution_options(synchronize_session="fetch")
        )
        up_user = await session.execute(query)
        await session.commit()
        return {"success": True}


async def get_user_email(user_email: str) -> UserReadLogin | None:
    async with db_helper.session_factory() as session:
        query = select(User.__table__.columns).where(User.email == user_email)
        user = await session.execute(query)
        return user.mappings().one_or_none()
