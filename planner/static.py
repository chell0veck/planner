import json
import os
from pathlib import Path

import calendarific
import songkick

skip_ctry = json.load(open(os.path.join(Path.cwd(), 'planner', 'static', 'skip_ctry.json')))
artists = json.load(open(os.path.join(Path.cwd(), 'planner', 'static', 'artists.json')))
events = songkick.load_events()
holidays = calendarific.load_holidays()
