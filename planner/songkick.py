"""Create songkick API interface.

Functions:

    get_events(tuple) -> list
    dump_events(dict) -> serialing to ../resources/songkick_events.pickle
    load_events(file) -> object

"""


import os
import datetime
import requests
import pickle
import json

from pathlib import Path

from tools import Event, timeit

API_KEY = open('.songkick_api_key', 'r').read()
CACHE = os.path.join(Path(__file__).parents[0], '_static_events.json')


def get_events_by_ids(artists):
    out = []

    for artist in set(artists):
        url = f'https://api.songkick.com/api/3.0/artists/{artist}/calendar.json?apikey={API_KEY}'
        res = requests.get(url).json()

        status_ok = res['resultsPage']['status'] == 'ok'
        events_exists = 'event' in res['resultsPage']['results']

        if status_ok and events_exists:
            events = res['resultsPage']['results']['event']
            out.append(events)

    return out


def get_events_by_name(name):
    """ Get events by dict {'artist name': artist_id}"""
    pass

arts = [521019, 201140]
d = {"Mono": 201140, 'smth': 222, 'abot': 33}


