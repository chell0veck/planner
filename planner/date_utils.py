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
    diff = (end_day-start_day-datetime.timedelta(days=max_range)).days + 2

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


def adjust_frame(start: 'datetime.date', end: 'datetime.date') -> 'tuple':
    """
    Extend given frame with nonworking days if such border with given start or end
       adjust_frame(datetime.date(2019, 6, 24), datetime.date(2019, 6, 27)) -> (datetime.date(2019, 6, 22), datetime.date(2019, 6, 30)):

    :param start: Start day of the frame
                June 24 2019 is Monday -> new start day is Saturday June 22 2019
    :param end: End day of the frame
                June 27 2019 is Thursday but June 28 is public holiday -> new end day is Sunday June 30 2019
    :return: Adjusted frame

    """

    new_start = start
    new_end = end

    while is_non_working(new_start - datetime.timedelta(days=1)):
        new_start -= datetime.timedelta(days=1)

    while is_non_working(new_end + datetime.timedelta(days=1)):
        new_end += datetime.timedelta(days=1)

    return new_start, new_end


frames = generate_frames()
print(help(adjust_frame))

