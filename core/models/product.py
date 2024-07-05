from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.orm import mapped_column

from core.models.base import Base

if TYPE_CHECKING:
    from core.models.basket import Basket


class Product(Base):
    name: Mapped[str] = mapped_column(String(50))
    description: Mapped[str] = mapped_column(String(100))
    price: Mapped[int] = mapped_column()

    basket: Mapped[list["Basket"]] = relationship(back_populates="product")
