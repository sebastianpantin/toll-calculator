from datetime import date
from pydantic import BaseModel, ConfigDict, UUID4, Field


class CreateTollEventRequest(BaseModel):
    registration_number: str = Field(min_length=6, max_length=6, pattern=r"^[A-Z]{3}\d{2}[A-Z0-9]$")
    time: date


class TollEvent(BaseModel):
    model_config = ConfigDict(from_attributes=True)  # orm mode
    id: UUID4
    registration_number: str = Field(min_length=6, max_length=6, pattern=r"^[A-Z]{3}\d{2}[A-Z0-9]$")
    time: date
