from sqlalchemy import engine
from sqlalchemy.ext.asyncio import (
    AsyncSession, 
    async_sessionmaker, 
    create_async_engine
)
from config import settings
from collections.abc import AsyncGenerator


DATABASE_URL = settings.get_db_url()
engine = create_async_engine(
    url=DATABASE_URL,
    echo=False
)
async_session_maker = async_sessionmaker(
    engine,
    expire_on_commit=False,
    autoflush=False
)

async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise