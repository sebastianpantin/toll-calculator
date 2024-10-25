from datetime import datetime
import pytest

from toll_calculator_backend.lib.toll_calculator import TollCalculator
from toll_calculator_backend.schemas.vehicle import Vehicle
from toll_calculator_backend.lib.time_utils import create_time


@pytest.mark.parametrize(
    "vehicle,dates,expected",
    [
        (Vehicle.Car, [], 0),  # No dates
        (Vehicle.Car, [create_time(6, 0), create_time(6, 22), create_time(6, 30)], 13),  # Max one fee in an hour
        (Vehicle.Car, [create_time(hour, 0) for hour in range(6, 19)], 60),  # Max fee for going past every hour
    ],
)
def test_get_toll_for_dates(vehicle: Vehicle, dates: list[datetime], expected: int):
    toll_calculator = TollCalculator()

    assert expected == toll_calculator.get_toll_fee_for_dates(vehicle, dates)


@pytest.mark.parametrize(
    "vehicle,date,expected",
    [
        (Vehicle.Car, create_time(5, 30), 0),
        (Vehicle.Car, create_time(15, 45), 18),
        (Vehicle.Motorbike, create_time(15, 45), 0),
        (Vehicle.Tractor, create_time(15, 45), 0),
        (Vehicle.Emergency, create_time(15, 45), 0),
        (Vehicle.Diplomat, create_time(15, 45), 0),
        (Vehicle.Foreign, create_time(15, 45), 0),
        (Vehicle.Military, create_time(15, 45), 0),
    ],
)
def test_get_toll_fee_for_different_times(vehicle: Vehicle, date: datetime, expected: int):
    toll_calculator = TollCalculator()
    assert expected == toll_calculator.get_toll_fee_for_date(vehicle, date)


@pytest.mark.parametrize(
    "vehicle,expected",
    [
        (Vehicle.Car, False),
        (Vehicle.Motorbike, True),
        (Vehicle.Tractor, True),
        (Vehicle.Emergency, True),
        (Vehicle.Diplomat, True),
        (Vehicle.Foreign, True),
        (Vehicle.Military, True),
    ],
)
def test_is_toll_free_vehicle(vehicle: Vehicle, expected: bool):
    toll_calculator = TollCalculator()
    # It's private but lets test it anyway
    assert expected == toll_calculator._is_toll_free_vehicle(vehicle)


@pytest.mark.parametrize(
    "date,expected",
    [
        (datetime(2024, 1, 1), True),  # New years day
        (datetime(2024, 1, 5), False),  # Twelfth night
        (datetime(2024, 1, 6), True),  # Epiphany
        (datetime(2024, 3, 29), True),  # Good Friday
        (datetime(2024, 4, 1), True),  # Easter monday
        (datetime(2024, 5, 1), True),  # Workers day
        (datetime(2024, 5, 9), True),  # Ascension day
        (datetime(2024, 6, 6), True),  # National day
        (datetime(2024, 6, 21), True),  # Midsummer eve
        (datetime(2024, 6, 22), True),  # Midsummer day
        (datetime(2024, 11, 2), True),  # All saints day
        (datetime(2024, 12, 24), True),  # Christmas eve
        (datetime(2024, 12, 25), True),  # Christmas day
        (datetime(2024, 12, 26), True),  # Second day of christmas
        (datetime(2024, 12, 31), True),  # New years eve
    ],
)
def test_is_toll_free_date(date: datetime, expected: bool):
    toll_calculator = TollCalculator()
    # It's private but lets test it to make sure
    assert expected == toll_calculator._is_toll_free_date(date)
