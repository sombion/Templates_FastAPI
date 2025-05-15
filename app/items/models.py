from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base


class Items(Base):
    __tablename__ = "items"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    