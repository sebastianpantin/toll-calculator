from calendar import SATURDAY, SUNDAY
from datetime import datetime, time

import holidays

from toll_calculator_backend.schemas.vehicle import Vehicle

swedish_holidays = holidays.SE()  # type: ignore[attr-defined]

LOW_FEE = 8
MED_FEE = 13
HIGH_FEE = 18


TOLL_FREE_VEHICLES: tuple[Vehicle, ...] = (
    Vehicle.Motorbike,
    Vehicle.Tractor,
    Vehicle.Emergency,
    Vehicle.Diplomat,
    Vehicle.Foreign,
    Vehicle.Military,
)

Rule = tuple[time, time, int]


class TimeRules:
    def __init__(self):
        self.rules: list[Rule] = [
            (time(6, 0), time(6, 29), LOW_FEE),  # 06:00 - 06:29
            (time(6, 30), time(6, 59), MED_FEE),  # 06:30 - 06:59
            (time(7, 0), time(7, 59), HIGH_FEE),  # 07:00 - 07:59
            (time(8, 0), time(8, 29), MED_FEE),  # 08:00 - 08:29
            (time(8, 30), time(14, 59), LOW_FEE),  # 08:30 - 14:59
            (time(15, 0), time(15, 29), MED_FEE),  # 15:00 - 15:29
            (time(15, 30), time(16, 59), HIGH_FEE),  # 15:30 - 16:59
            (time(17, 0), time(17, 59), MED_FEE),  # 17:00 - 17:59
            (time(18, 0), time(18, 29), LOW_FEE),  # 18:00 - 18:29
        ]

    def get_fee(self, hour: int, minute: int):
        current_time = time(hour, minute)
        for start_time, end_time, fee in self.rules:
            if start_time <= current_time <= end_time:
                return fee
        return 0


class TollCalculator:
    def __init__(self):
        self.max_fee = 60

    """
    No function overloads in python so we have separate functions for multiple or single dates
    """

    """
        The vehicle can only be tolled once per hour, with the highest fee in that timespan
    """

    def get_toll_fee_for_dates(self, vehicle: Vehicle, dates: list[datetime]) -> int:
        # No point in looping over all dates if toll free vehicle

        if self._is_toll_free_vehicle(vehicle) or len(dates) == 0:
            return 0

        total_fee = 0
        max_fee_in_hour = 0
        start_date = dates[0]

        for date in dates:
            next_fee = self.get_toll_fee_for_date(vehicle, date)
            diff_minutes = (date - start_date).total_seconds() / 60

            if diff_minutes <= 60:
                max_fee_in_hour = max(max_fee_in_hour, next_fee)
            else:
                total_fee += max_fee_in_hour
                start_date = date
                max_fee_in_hour = next_fee

            if total_fee >= 60:
                return 60

        total_fee += max_fee_in_hour
        return min(total_fee, 60)

    def get_toll_fee_for_date(self, vehicle: Vehicle, date: datetime) -> int:
        if self._is_toll_free_vehicle(vehicle) or self._is_toll_free_date(date):
            return 0
        time_rules = TimeRules()
        return time_rules.get_fee(date.hour, date.minute)

    # underscore for "private"
    def _is_toll_free_vehicle(self, vehicle: Vehicle) -> bool:
        return vehicle in TOLL_FREE_VEHICLES

    # underscore for "private"
    def _is_toll_free_date(self, date: datetime) -> bool:
        week_day = date.weekday()

        if week_day == SATURDAY or week_day == SUNDAY:
            return True

        return date in swedish_holidays
