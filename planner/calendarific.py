import datetime
import requests
import pickle
import os

from pathlib import Path


api_key = open(os.path.join(Path(__file__).parents[0], 'config', '.calendarific_api_key'), 'r').read()
params = {'api_key': api_key, 'country': 'ua', 'year': datetime.datetime.today().year}
cache = os.path.join(Path(__file__).parents[0], 'static', 'holidays.pickle')
url = 'https://calendarific.com/api/v2/holidays'


def get_holidays():
    res = requests.get(url=url, params=params)
    out = []

    if res.status_code == 200:
        holidays = res.json()['response']['holidays']

        for holiday in holidays:
            if 'National holiday' in holiday['type']:
                _date = datetime.datetime.strptime(holiday['date']['iso'], '%Y-%m-%d')

                if _date.weekday() not in (5, 6):
                    out.append(_date)
    return out


def dump_holidays():
    """ Dump holidays """
    holidays = get_holidays()

    with open(cache, 'wb') as f:
        pickle.dump(holidays, f)


def load_holidays():
    """ Load holidays from the file"""
    with open(cache, 'rb') as f:
        return pickle.load(f)
