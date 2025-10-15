import fastf1
import pandas as pd

from fastf1.ergast import Ergast

event = fastf1.get_session(2023, "Monza", "R")

event.load()


def getDriverLaptimes(session, driver):
    """
    Returns the lap times of a driver in a given F1 session.

    Args:
        session (fastf1.Session): F1 Session object
        driver (str): Driver's three letter code ex: 'VER'

    Returns:
        List (List[Tuple[int, float]]): List of tuples as (Lap Number, Time in Seconds)
    """

    laps = session.laps.pick_driver(driver)
    laps["LapTime"] = laps["LapTime"].dt.total_seconds()
    lapTimes = list(zip(laps["LapNumber"].tolist(), laps["LapTime"].tolist()))
    return lapTimes
