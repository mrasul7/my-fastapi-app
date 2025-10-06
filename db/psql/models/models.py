
from sqlalchemy import (
    BigInteger, 
    String, 
    Integer
)
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import (
    DeclarativeBase, 
    Mapped, 
    mapped_column
)
from db.psql.models.columns import create_at

class Base(AsyncAttrs, DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'users'
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    telegram_id: Mapped[int] = mapped_column(BigInteger, unique=True, index=True, nullable=False)
    phone_number: Mapped[str | None] = mapped_column(String(15), unique=True, nullable=True)
    name: Mapped[str] = mapped_column(String(50))
    username: Mapped[str | None] = mapped_column(String(50))
    created_at: Mapped[create_at]
