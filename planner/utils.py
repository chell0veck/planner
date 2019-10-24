import json
import datetime
import holidays
from config import ARTISTS


def is_nonwork(date):
    ua_holidays = holidays.UA(years=date.year)

    if date in ua_holidays:
        return True

    if date.weekday() in (5, 6):
        return True

    if date.weekday() == 0 and date-datetime.timedelta(days=1) in ua_holidays:
        return True

    if date.weekday() == 0 and date-datetime.timedelta(days=2) in ua_holidays:
        return True

    return False


def load_artist_from_file(file=ARTISTS):

    with open(file) as f:
        artists = json.load(f)
        return artists
