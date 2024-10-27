import random
from datetime import datetime, timedelta

from sqlmodel import Session, exists

from toll_calculator_backend.config.database import engine
from toll_calculator_backend.models.toll_event import TollEvent
from toll_calculator_backend.schemas.vehicle import Vehicle

from .logger import logger_config

n_events = 50
n_unique_reg_numbers = 10

logger = logger_config(__name__)


def create_toll_events():
    start_time = datetime(2020, 1, 1)
    logger.info(f"Generating mock data, with {n_events * n_events} events")
    with Session(engine) as session:
        data_exists = session.query(exists().where(TollEvent.id.isnot(None))).scalar()

        if not data_exists:
            for i in range(0, n_unique_reg_numbers):
                for j in range(0, n_events):
                    # Generate the registration number with leading zeros as needed
                    reg_number = f"AAA0{i:02d}"

                    # Randomly choose an interval type to add (minutes, hours, or days)
                    interval_type = random.choice(["minutes", "hours", "days"])

                    # Set a random increment within a reasonable range for each interval type
                    if interval_type == "minutes":
                        event_time = start_time + timedelta(minutes=random.randint(1, 59))
                    elif interval_type == "hours":
                        event_time = start_time + timedelta(hours=random.randint(1, 23))
                    else:  # 'days'
                        event_time = start_time + timedelta(days=random.randint(1, 7))

                    # Create the TollEvent instance with the unique timestamp
                    toll_event = TollEvent(registration_number=reg_number, vehicle=Vehicle.Car, time=event_time)

                    # Add the TollEvent to the session
                    session.add(toll_event)
                    session.commit()

                    # Update start_time to event_time to ensure each new event has a later timestamp
                    start_time = event_time
    logger.info("Generating mock data done")
