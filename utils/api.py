from fastapi import HTTPException, Header, status
from secrets import compare_digest
from config import settings

async def verify_api_token(token: str = Header(..., alias="X-API-Token")) -> bool:
    if not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Необходимо ввести API токен"
        )
    if not compare_digest(token, settings.API_TOKEN):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Невалидный API токен"
        )
    
    return True