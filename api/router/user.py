from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from api.schemas.user import UserMessage
from sqlalchemy import select
from utils.api import verify_api_token
from core.psql import get_db
from db.psql.models.models import User
from core.bot import bot

router = APIRouter(
    tags=["User"],
    prefix="/user"
)


@router.post("/send_message")
async def send_message(
    request: UserMessage, 
    session: AsyncSession = Depends(get_db),
    token: str = Depends(verify_api_token)
) -> None:
    result = await session.execute(select(User).where(User.phone_number == request.phone_number))
    user = result.scalar_one_or_none()
    
    if user:
        await bot.send_message(
            chat_id=user.telegram_id,
            text=request.text
        )
