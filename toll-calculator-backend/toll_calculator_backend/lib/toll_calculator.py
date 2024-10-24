import datetime


class TollCalculator:
    """
    Renamed from get_toll_fee to better reflect what it actually does
    """

    # TODO: Add types
    def get_toll_fee_between_dates(self, vehicle, dates: list[datetime.date]) -> int:
        if len(dates) == 0:
            return 0

        return 1

    def get_toll_fee_for_date(self, date: datetime.date, vehicle) -> int:
        return 1

    def is_toll_free_vehicle(self, vehicle) -> bool:
        return False

    def is_toll_free_date(self, date: datetime.date) -> bool:
        return False
