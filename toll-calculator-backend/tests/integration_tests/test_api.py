import pytest
from datetime import datetime, time
from fastapi.testclient import TestClient
from sqlmodel import Session, SQLModel, create_engine
from sqlmodel.pool import StaticPool

from toll_calculator_backend.models.toll_event import TollEvent
from toll_calculator_backend.config.database import get_session
from toll_calculator_backend.main import create_app


@pytest.fixture(name="session")
def session_fixture():
    engine = create_engine("sqlite://", connect_args={"check_same_thread": False}, poolclass=StaticPool)
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        yield session


@pytest.fixture(name="client")
def client_fixture(session: Session):
    def get_session_override():
        return session

    app = create_app()
    app.dependency_overrides[get_session] = get_session_override

    client = TestClient(app)
    yield client
    app.dependency_overrides.clear()


def test_register_event(client: TestClient):
    response = client.post(
        "/api/toll/register-toll-event",
        json={
            "registration_number": "PYW200",
            "vehicle": "car",
            "time": "2024-10-27T15:39:18",
        },
    )
    response_data = response.json()
    data = response_data["event"]

    assert response.status_code == 200
    assert data["registration_number"] == "PYW200"
    assert data["vehicle"] == "car"
    assert data["time"] == "2024-10-27T15:39:18"


def test_register_event_missing_data(client: TestClient):
    response = client.post(
        "/api/toll/register-toll-event",
        json={
            "registration_number": "PYW200",
            "time": "2024-10-27T15:39:18",
        },
    )

    assert response.status_code == 422


def test_register_event_invalid_reg_number(client: TestClient):
    response = client.post(
        "/api/toll/register-toll-event",
        json={
            "registration_number": "PMAA00",
            "vehicle": "car",
            "time": "2024-10-27T15:39:18",
        },
    )

    assert response.status_code == 422
