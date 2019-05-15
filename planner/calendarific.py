import datetime
import requests
import json
import os

from pathlib import Path


API_KEY = open('.calendarific_api_key', 'r').read()
PARAMS = {'api_key': API_KEY, 'country': 'ua', 'year': datetime.datetime.today().year}
CACHE = os.path.join(Path(__file__).parents[0], '_static_holidays.json')
URL = 'https://calendarific.com/api/v2/holidays'


def get_holidays():
    res = requests.get(url=URL, params=PARAMS)
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


def dump_holidays():
    """ Dump holidays """
    holidays = get_holidays()

    with open(CACHE, 'w') as f:
        json.dump(holidays, f)


def load_holidays():
    """ Load holidays from the file"""
    with open(CACHE, 'r') as f:
        return json.load(f)