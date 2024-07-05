from fastapi import APIRouter
from fastapi import HTTPException
from fastapi import Response

from core.auth.auth_user import authenticate_user, create_access_token
from core.schemas.user import UserCreate, UserRead, UserReadLogin
from crud.user import create_user as user_create
from crud.user import get_user_email

router = APIRouter(
    tags=["Auth"],
    prefix="/v1"
)


@router.post("/register")
async def register_user(
    user_in: UserCreate,
) -> UserRead:
    existing_user = await get_user_email(user_in.email)
    if existing_user:
        raise HTTPException(status_code=500)
    return await user_create(user_in=user_in)


@router.post("/login")
async def login_user(
        response: Response,
        user_in: UserReadLogin
):
    user = await authenticate_user(
        user_in.email,
        user_in.password
    )
    access_token = create_access_token({"sub": str(user.id)})
    response.set_cookie("access_token", access_token, httponly=True)
    return {"access_token": access_token}
