from datetime import datetime
from typing import Annotated
from fastapi import APIRouter, Query, Depends
from toll_calculator_backend.schemas.toll import TollEventCreate
from toll_calculator_backend.services.toll_service import TollService
from sqlmodel import Session
from toll_calculator_backend.config.database import get_session

router = APIRouter(prefix="/api/toll")


@router.get("/get-toll-fee-by-day")
def get_toll_fee(
    registration_number: Annotated[str, Query(max_length=6, min_length=6, pattern=r"^[A-Z]{3}\d{2}[A-Z0-9]$")],
    day: Annotated[datetime, Query()],
    session: Session = Depends(get_session),
):
    toll_service = TollService(session)
    total_toll = toll_service.get_toll_fee_for_day(registration_number, day)
    return {"total_toll": total_toll}


@router.post("/register-toll-event")
def register_toll_event(request: TollEventCreate, session: Session = Depends(get_session)):
    toll_service = TollService(session)
    created_event = toll_service.create_toll_event(request)
    return {"event": created_event}
