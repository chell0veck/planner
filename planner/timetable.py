import datetime
import requests
import json
import os

from pathlib import Path


api_key = open('.calendarific_api_key', 'r').read()
params = {'api_key': api_key, 'country': 'ua', 'year': datetime.datetime.today().year}
json_cache = os.path.join(Path(__file__).parents[0], '_static_holidays.json')
url = 'https://calendarific.com/api/v2/holidays'


def get_holidays():
    res = requests.get(url=url, params=params)
    out = []

    if res.status_code == 200:
        holidays = res.json()['response']['holidays']

        for holiday in holidays:
            if 'National holiday' in holiday['type']:
                str_date = holiday['date']['iso']
                fmt_date = datetime.datetime.strptime(holiday['date']['iso'], '%Y-%m-%d').date()

                if fmt_date.weekday() not in (5, 6):
                    out.append(str_date)
    return out


def get_nonwork(year=datetime.datetime.today().year):
    raw_holidays = load_holidays()
    fmt_holidays = [convert_date(dt) for dt in raw_holidays]
    weekends = [(datetime.date(year, 1, 1) + datetime.timedelta(i)) for i in range(365)
                if (datetime.date(year, 1, 1) + datetime.timedelta(i)).weekday() in (5, 6)
                and (datetime.date(year, 1, 1) + datetime.timedelta(i)).year == year]
    nonwork = fmt_holidays + weekends

    return sorted(set(nonwork))


def dump_holidays():
    """ Dump holidays """
    holidays = get_holidays()

    with open(json_cache, 'w') as f:
        json.dump(holidays, f)


def load_holidays():
    """ Load holidays from the file"""
    with open(json_cache, 'r') as f:
        return json.load(f)


def convert_date(date_time_str):
    date_time_obj = datetime.datetime.strptime(date_time_str, '%Y-%m-%d').date()
    return date_time_obj
