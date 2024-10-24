from enum import Enum


class Vehicle(str, Enum):
    Car = "car"
    Motorbike = "motorbike"
    Tractor = "tractor"
    Emergency = "emergency"
    Diplomat = "diplomat"
    Foreign = "foreign"
    Military = "military"
