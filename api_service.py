import uvicorn

from api.router.user import router as user
from core.api import app
from core.logger import api_logger

app.include_router(router=user)


if __name__ == "__main__":
    try:
        uvicorn.run(
            app=app,
            host="0.0.0.0",
            port=8000
        )
    except KeyboardInterrupt:
        api_logger.info('Выход')