from datetime import datetime
from pydantic import BaseModel, UUID4, Field 
from .vehicle import Vehicle


class TollEventCreate(BaseModel):
    registration_number: str = Field(min_length=6, max_length=6, pattern=r"^[A-Z]{3}\d{2}[A-Z0-9]$")
    vehicle: Vehicle
    time: datetime


class TollEventOutput(BaseModel):
    id: UUID4
    registration_number: str = Field(min_length=6, max_length=6, pattern=r"^[A-Z]{3}\d{2}[A-Z0-9]$")
    vehicle: Vehicle = Vehicle.Car
    time: datetime
