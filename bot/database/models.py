from sqlalchemy import DateTime, Integer, String, Boolean, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    id_telegram: Mapped[int] = mapped_column(Integer, unique=True)
    nik_name_telegram: Mapped[int] = mapped_column(String, default=None)

    use_runtime: Mapped[bool] = mapped_column(Boolean, default=False)
    reqests_vpn: Mapped[bool] = mapped_column(Boolean, default=False)

    ip_client: Mapped[str] = mapped_column(String, default='0')

    created: Mapped[DateTime] = mapped_column(DateTime, default=func.now())