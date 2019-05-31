import datetime

import holidays

from utils import Day


def get_non_work(year=datetime.datetime.today().year):
    """
    To be defined
    :param year:
    :return:
    """

    _holidays = [dt for dt in holidays.UA(years=year)]
    first_day = datetime.date(year, 1, 1)
    weekdays = [(first_day + datetime.timedelta(i)) for i in range(370)
                if (first_day + datetime.timedelta(i)).weekday() in (5, 6)
                and (first_day + datetime.timedelta(i)).year == year]

    non_working_days = _holidays + weekdays

    return sorted(non_working_days)


def generate_year_dates(days):
    result = days
    start = datetime.date(2019, 1, 1)
    days_with_events = [day.date for day in days]
    all_days = [start + datetime.timedelta(days=n) for n in range(365)]
    days_without_events = [Day(day, False, False) for day in all_days if day not in days_with_events]
    result.extend(days_without_events)

    return result


def generate_frames(start_day=datetime.date.today(), end_day=None, max_range=20):
    result = []
    end_day = end_day if end_day is not None else datetime.date(start_day.year, 12, 31)
    diff = (end_day-start_day-datetime.timedelta(days=max_range)).days

    for start in range(diff):
        new_start_day = start_day + datetime.timedelta(days=start)

        for end in range(1, max_range):
            new_end_day = new_start_day + datetime.timedelta(days=end)
            result.append((new_start_day, new_end_day))

    return result


def is_non_working(date: 'datetime.date') -> 'bool':
    """
    Return True if given date is a weekend or public holiday in Ukraine
    :param date:
    :return: bool
    """
    if date.weekday() in (5, 6):
        return True

    if date in holidays.UA(years=date.year):
        return True

    return False


frames = generate_frames()

for frame in frames:
    print(frame)
