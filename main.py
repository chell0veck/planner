"""
Entry point of a program. So far just change the view model from md lib
"""

import songkick as sk
import utils as ut
import datetime

events = sk.load_events()
frame_str = datetime.date.today()
frame_end = max(event.date for event in events)
dates = ut.generate_dates(frame_str, frame_end)
emap = ut.build_events_map(events)
gomodata = ut.wrap_days(dates, emap)

for data in gomodata:
    print(data)

    # if data.nonwork and data.event:
    #     print('{:<10}'.format(data.date.strftime("%A")), data.event)
