from datetime import datetime

from sqlmodel import Session, and_

from toll_calculator_backend.models.toll_event import TollEvent
from toll_calculator_backend.schemas.toll import TollEventCreate, TollEventOutput


class TollRepository:
    def __init__(self, session: Session):
        self.session = session

    def create_toll_event(self, create_toll_event: TollEventCreate) -> TollEventOutput:
        toll_event = TollEvent(**create_toll_event.model_dump(exclude_none=True))
        self.session.add(toll_event)
        self.session.commit()
        self.session.refresh(toll_event)
        return TollEventOutput(**toll_event.__dict__)

    def get_toll_events_between_dates_and_registration_number(
        self, registration_number: str, start_date: datetime, end_date: datetime
    ) -> list[TollEventOutput]:
        events = (
            self.session.query(TollEvent).filter(and_(TollEvent.time >= start_date, TollEvent.time <= end_date)).all()
        )
        return [TollEventOutput(**event.__dict__) for event in events]
