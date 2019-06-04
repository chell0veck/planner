import datetime

import holidays


def generate_frames(start_day: 'datetime.date' = None, end_day: 'datetime.date' = None, max_range: 'int' = 20) -> list:
    """
    Return list of tuples with possible ranges withing given start, edn and max range
    :param start_day: start of the period
    :param end_day: end of the period
    :param max_range: max len of range
    :return: list
    """
    start_day = start_day if start_day else datetime.date.today()
    end_day = end_day if end_day is not None else datetime.date(start_day.year + 1, 1, 1)
    diff = (end_day-start_day-datetime.timedelta(days=max_range)).days + 2

    for start in range(diff):
        new_start_day = start_day + datetime.timedelta(days=start)

        for end in range(1, max_range):
            new_end_day = new_start_day + datetime.timedelta(days=end)
            yield (new_start_day, new_end_day)


def is_non_working(date: 'datetime.date') -> 'bool':
    """
    Return True if given date is a weekend or public holiday in Ukraine

    :param date: Date to check
    :return : True if date is non working, False otherwise

     Examples:
        >>> is_non_working(datetime.date(2019, 6, 28)) # Public holiday
        True
        >>> is_non_working(datetime.date(2019, 6, 30)) # Sunday
        True
        >>> is_non_working(datetime.date(2019, 7, 1))  # Monday
        False

    """
    if date.weekday() in (5, 6):
        return True

    if date in holidays.UA(years=date.year):
        return True

    return False


def adjust_frame(frame: 'tuple') -> 'tuple':
    """
    Extend given frame with nonworking days if such border with given start or end
       adjust_frame(datetime.date(2019, 6, 24), datetime.date(2019, 6, 27)) -> (datetime.date(2019, 6, 22), datetime.date(2019, 6, 30)):

    :param frame: Date frame (tuple of datetime.date objects)

    :return: Adjusted frame

    """
    new_start, new_end = frame

    while is_non_working(new_start - datetime.timedelta(days=1)):
        new_start -= datetime.timedelta(days=1)

    while is_non_working(new_end + datetime.timedelta(days=1)):
        new_end += datetime.timedelta(days=1)

    return new_start, new_end


frames = generate_frames()

