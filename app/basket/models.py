from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base


class Basket(Base):
    __tablename__ = "basket"

    id: Mapped[int] = mapped_column(primary_key=True)
    users_id: Mapped[int]
    items_id: Mapped[int]