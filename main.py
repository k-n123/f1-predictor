import fastf1

fastf1.Cache.enable_cache("f1_cache")

import pandas as pd

from visualizer import Visualizer

from fastf1.ergast import Ergast

event = fastf1.get_event(2023, "Monza")


verstappen = Visualizer(event, "VER")
verstappen.plotFastestLaps(event.get_session("R"))
