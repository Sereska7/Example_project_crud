from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.orm import mapped_column

from core.models.base import Base

if TYPE_CHECKING:
    from core.models import User
    from core.models import Product


class Basket(Base):
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"))

    user: Mapped["User"] = relationship(back_populates="basket")
    product: Mapped["Product"] = relationship(back_populates="basket")
