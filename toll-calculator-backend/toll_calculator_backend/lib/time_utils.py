from datetime import datetime, time


def create_time(hour: int, minute: int) -> datetime:
    """
    Creates a datetime from just hour and minute.
    It uses current date for year, month and day
    """

    return datetime.combine(datetime(2024, 10, 24), time(hour, minute))
