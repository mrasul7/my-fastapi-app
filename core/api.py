from contextlib import asynccontextmanager
from fastapi import FastAPI
from core.logger import api_logger

@asynccontextmanager
async def lifespan(app: FastAPI):
    api_logger.info("=== App started ===")
    yield
    api_logger.info("=== App stopped ===")

app = FastAPI(lifespan=lifespan)