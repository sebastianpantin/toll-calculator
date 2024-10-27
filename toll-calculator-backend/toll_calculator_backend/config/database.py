from sqlmodel import create_engine, Session, SQLModel

from .settings import get_database_settings, get_settings

app_settings = get_settings()
database_settings = get_database_settings()

if app_settings.DEBUG:
    SQLALCHEMY_DATABASE_URL = database_settings.SQLITE_CONNECTION_STRING
else:
    SQLALCHEMY_DATABASE_URL = database_settings.POSTGRES_CONNECTION_STRING

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    echo=True,
    connect_args={"check_same_thread": False},
)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine, autocommit=False, autoflush=False) as session:
        yield session
