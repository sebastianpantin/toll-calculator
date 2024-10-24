import os
from functools import lru_cache

from pydantic_settings import BaseSettings


class DatabaseSettings(BaseSettings):
    name: str = "fastapi_db"
    user: str = "postgres"
    password: str = "postgres"
    host: str = "localhost"
    port: int = 5432

    class Config:
        env_prefix = "POSTGRES_DB_"

    @property
    def url(self) -> str:
        return f"postgresql://{self.user}:{self.password}@{self.host}:{self.port}/{self.name}"

    @property
    def async_url(self) -> str:
        return f"postgresql+asyncpg://{self.user}:{self.password}@{self.host}:{self.port}/{self.name}"


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
