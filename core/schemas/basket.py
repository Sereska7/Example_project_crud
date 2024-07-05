from pydantic import BaseModel, EmailStr


class BasketBase(BaseModel):
    user_id: int
    product_id: int


class BasketCreate(BasketBase):
    pass


class BasketRead(BasketBase):

    id: int
    all_price: int


class BasketUpdatePartial(BasketCreate):
    id: int | None = None
    user_id: int | None = None
    product_id: int | None = None


# class BasketReadAll(BaseModel):
#     user_email: EmailStr
#     product_name: str

