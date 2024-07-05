from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    email: EmailStr


class UserCreate(UserBase):

    password: str


class UserUpdatePartial(UserCreate):
    email: EmailStr | None = None
    password: str | None = None


class UserRead(UserBase):

    id: int


class UserReadLogin(UserBase):
    email: EmailStr
    password: str
