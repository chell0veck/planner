"""
Entry point of a program. So far just change the view model from md lib
"""

import datetime

import songkick as sk
import utils as ut


def wrap_events_into_days(events, holidays):
    result = []
    visited = []

    for event in events:
        if event.date in holidays:
            result.append(ut.Day(event.date, event, True))
            visited.append(event.date)
        else:
            result.append(ut.Day(event.date, event, False))

    for holiday in holidays:
        if holiday not in visited:
            result.append(ut.Day(holiday, None, True))

    return result


def generate_year_dates(days):
    result = days
    start = datetime.date(2019, 1, 1)
    days_with_events = [day.date for day in days]
    all_days = [start + datetime.timedelta(days=n) for n in range(365)]
    days_without_events = [ut.Day(day, False, False) for day in all_days if day not in days_with_events]
    result.extend(days_without_events)

    return result



events = sk.load_events()
holidays = ut.get_nonwork()
_days = wrap_events_into_days(events, holidays)
days = generate_year_dates(_days)


for day in days:
    if day.event and day.event.artist == 'Tool':
        print(day, day.nonwork)
