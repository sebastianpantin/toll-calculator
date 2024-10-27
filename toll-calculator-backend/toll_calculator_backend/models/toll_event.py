import uuid
from sqlalchemy import Column
from datetime import datetime
from toll_calculator_backend.schemas.vehicle import Vehicle
from sqlmodel import Field, SQLModel, Enum


class TollEvent(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    vehicle: Vehicle = Field(sa_column=Column(Enum(Vehicle)))
    registration_number: str = Field(index=True, max_length=6, min_length=6, regex=r"^[A-Z]{3}\d{2}[A-Z0-9]$")
    time: datetime = Field(index=True)
