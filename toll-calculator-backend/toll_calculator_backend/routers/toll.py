from datetime import date
from typing import Annotated
from fastapi import APIRouter, Query
from toll_calculator_backend.schemas.toll import CreateTollEventRequest
from toll_calculator_backend.schemas.vehicle import Vehicle

router = APIRouter(prefix="/api/toll")


@router.get("/get-toll-fee")
def get_toll_fee(vehicle: Vehicle, dates: Annotated[list[date], Query()] = []):
    return {"total_toll": 0}


@router.post("/register-toll-event")
def register_toll_event(request: CreateTollEventRequest):
    return 0
