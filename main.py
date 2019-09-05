"""
Entry point of a program. So far just change the view model from md lib
"""
from collections import defaultdict
from itertools import combinations

import songkick as sk
import utils as ut
import models as md
import datetime
import cProfile


events = sk.load_events()
_start = datetime.date.today()
_end = max(event.date for event in events)
dates = ut.generate_dates(_start, _end)
emap = ut.build_events_map(events)
data = ut.wrap_days(dates, emap)

md.view_by_month(events)
