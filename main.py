"""
Entry point of a program. So far just change the view model from md lib
"""

import datetime

import songkick as sk
import date_utils as ut
import utils as ud

events = sk.load_events()
holidays = ut.get_non_work()
_days = ud.wrap_events_into_days(events, holidays)
year = ut.generate_year_dates(_days)
sd = datetime.date.today()
ed = sd + datetime.timedelta(days=20)


def generate_frame(start_day, end_day, days):
    t = [ds for ds in days if start_day <= ds.date <= end_day]
    o = sorted(t, key=lambda d: d.date)

    for i in o:
        print(i)


generate_frame(sd, ed, _days)
