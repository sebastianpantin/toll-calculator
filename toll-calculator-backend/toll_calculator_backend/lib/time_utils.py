from datetime import date, datetime, time


def create_time(hour: int, minute: int) -> date:
    """
    Creates a datetime from just hour and minute.
    It uses current date for year, month and day
    """

    return datetime.combine(datetime.today(), time(hour, minute))
