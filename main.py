"""
Entry point of a program. So far just change the view model from md lib
"""

import songkick as sk
from utils import Day
import datetime
import holidays


events = sk.load_events()


def is_nonwork(date):
    _holidays = holidays.UA(years=2019)

    if date in _holidays:
        return True

    if date.weekday() in (5, 6):
        return True

    return False


def default(events, year=2019):
    first_day = datetime.date(year, 1, 1)

    for i in range(365):
        day = first_day + datetime.timedelta(days=i)

        # print(day, is_nonwork(day), day.strftime('%A'))

        nonwork = is_nonwork(day)

        if nonwork:
            print(day, day.strftime('%A'))
#

default(events, 2019)