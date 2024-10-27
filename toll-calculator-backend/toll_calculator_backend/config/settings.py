import os
from functools import lru_cache

from pydantic_settings import BaseSettings


class DatabaseSettings(BaseSettings):
    """
    Database settings
    """

    # SqlLite
    SQLITE_CONNECTION_STRING: str = "sqlite:///database.db"

    # PostgreSQL
    POSTGRESS_USER: str | None = os.environ.get("POSTGRES_USER", None)
    POSTGRESS_PASSWORD: str | None = os.environ.get("POSTGRES_PASSWORD", None)
    POSTGRES_CONNECTION_STRING: str = f"postgresql://{POSTGRESS_USER}:{POSTGRESS_PASSWORD}@postgresserver/db"


class Settings(BaseSettings):
    """
    Application settings.
    """

    DEBUG: bool = os.environ.get("DEBUG", "True") == "True"
    NAME: str = os.environ.get("NAME", "toll-backend")


@lru_cache(maxsize=1)
def get_settings():
    return Settings()


@lru_cache()
def get_database_settings() -> DatabaseSettings:
    return DatabaseSettings()
