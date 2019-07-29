"""
Entry point of a program. So far just change the view model from md lib
"""
import datetime

import songkick as sk
import utils as ut
import models as md


events = sk.load_events()
frame_str = datetime.date.today()
frame_end = max(event.date for event in events)
dates = ut.generate_dates(frame_str, frame_end)
emap = ut.build_events_map(events)
gomodata = ut.wrap_days(dates, emap)

md.view_by_month(events)


