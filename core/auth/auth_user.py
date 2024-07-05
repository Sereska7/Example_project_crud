from jose import jwt
from datetime import datetime, timedelta
from fastapi import HTTPException

from pydantic import EmailStr

from core.auth.utils import verify_password
from core.config import settings
from crud.user import get_user_email


def create_access_token(date: dict) -> str:
    to_encode = date.copy()
    expire = datetime.now() + timedelta(minutes=10)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode, settings.SECRET_KEY, settings.ALGORITHM
    )
    return encoded_jwt


async def authenticate_user(email: EmailStr, password: str):
    user = await get_user_email(user_email=email)
    if not (user and verify_password(password, user.password)):
        raise HTTPException(status_code=500)
    return user
