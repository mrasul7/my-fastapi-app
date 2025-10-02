from core.psql import engine
from db.psql.models.models import Base

async def init_psql() -> bool:
    async with engine.begin() as connect:
        await connect.run_sync(Base.metadata.create_all)
    return True