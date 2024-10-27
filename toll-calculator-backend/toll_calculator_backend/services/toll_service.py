from datetime import datetime, time

from sqlmodel import Session

from toll_calculator_backend.schemas.toll import TollEventCreate
from toll_calculator_backend.lib.toll_calculator import TollCalculator
from toll_calculator_backend.repository.toll_repository import TollRepository


class TollService:
    def __init__(self, session: Session):
        """
        Init the service
        """
        self.repository = TollRepository(session)
        self.calculator = TollCalculator()

    def get_toll_fee_for_day(self, registration_number: str, day: datetime) -> int:
        start_date = day
        end_date = datetime.combine(start_date, time.max)
        toll_events = self.repository.get_toll_events_between_dates_and_registration_number(
            registration_number, start_date, end_date
        )
        if len(toll_events) == 0:
            return 0
        vehicle = toll_events[0].vehicle
        dates = [event.time for event in toll_events]

        toll_fee = self.calculator.get_toll_fee_for_dates(vehicle, dates)
        return toll_fee

    def create_toll_event(self, toll_event: TollEventCreate):
        return self.repository.create_toll_event(toll_event)
