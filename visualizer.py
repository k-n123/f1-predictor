import fastf1
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


class Visualizer:
    def __init__(self, event, driver):
        # Gives all data as charts and stuff from a driver's event (all sessions)
        self.event = event
        self.driver = driver

    def getDriverLaptimes(self, session, driver):
        """
        Returns the lap times of a driver in a given F1 session.

        Args:
            session (fastf1.Session): F1 Session object
            driver (str): Driver's three letter code ex: 'VER'

        Returns:
            List (List[Tuple[int, float]]): List of tuples as (Lap Number, Time in Seconds)
        """
        session.load()
        laps = session.laps.pick_driver(driver)
        laps["LapTime"] = laps["LapTime"].dt.total_seconds()
        lapTimes = (laps["LapNumber"].tolist(), laps["LapTime"].tolist())
        return lapTimes

    def plotDriverLaptimes(self):
        """
        Plots the lap times of a driver in a given F1 Race (Grand Prix)

        Args:
            session (fastf1.Session): F1 Session object derived from self.event

        Returns:
            None
            Data Plot: Lap Number vs Lap Time (seconds)
        """

        lapNumbers, lapTimes = self.getDriverLaptimes(
            self.event.get_session("R"), self.driver
        )
        plt.scatter(lapNumbers, lapTimes)
        plt.xlabel("Lap Number")
        plt.ylabel("Lap Time (seconds)")
        plt.show()

    # All Charts for driver from for specified session
    def plotAllSession(self, session):
        self.plotDriverLaptimes(session, self.driver)
