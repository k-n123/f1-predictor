import fastf1

fastf1.Cache.enable_cache("f1_cache")

import pandas as pd

from visualizer import Visualizer

from fastf1.ergast import Ergast

event = fastf1.get_session(2023, "Monza", "R")

event.load()

verstappen = Visualizer(event, "VER")
verstappen.plotDriverLaptimes()
