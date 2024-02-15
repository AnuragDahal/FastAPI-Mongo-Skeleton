from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer
from core.database import Base


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
