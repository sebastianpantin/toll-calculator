from contextlib import asynccontextmanager

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from toll_calculator_backend.config.database import create_db_and_tables
from toll_calculator_backend.config.settings import get_settings
from toll_calculator_backend.lib.generate_mock_data import create_toll_events
from toll_calculator_backend.lib.logger import logger_config
from toll_calculator_backend.routers import toll

settings = get_settings()

logger = logger_config(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    create_toll_events()
    logger.info("App startup")
    yield
    logger.info("App shutdown")


def create_app():
    app = FastAPI(debug=settings.DEBUG, title=settings.NAME, lifespan=lifespan)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(toll.router)
    return app
