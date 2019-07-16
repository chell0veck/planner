"""
Entry point of a program. So far just change the view model from md lib
"""

import songkick as sk
import utils as ut
import datetime
import models as md
import holidays


events = sk.load_events()
frame_str = datetime.date.today()
frame_end = max(event.date for event in events)
dates = ut.generate_dates(frame_str, frame_end)
emap = ut.build_events_map(events)
_map = list(emap)
gomodata = ut.wrap_days(dates, emap)



def test():
    start = datetime.date(2019, 1, 1)

    for i in range(365):
        day = start + datetime.timedelta(days=i)
        day_is_holiday = ut.is_nonwork(day)

        if day_is_holiday:
            if day.strftime('%A') not in ('Saturday', 'Sunday'):
                print(day.strftime('%b %d %A'))




test()


