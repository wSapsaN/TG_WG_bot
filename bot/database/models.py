from sqlalchemy import DateTime, Integer, String, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    id_telegram: Mapped[int] = mapped_column(Integer, unique=True)
    nik_name_telegram: Mapped[int] = mapped_column(String, default=None)
    created: Mapped[DateTime] = mapped_column(DateTime, default=func.now())