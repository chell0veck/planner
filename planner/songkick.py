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


def get_events_by_id(artist_id):
    url = f'https://api.songkick.com/api/3.0/artists/{artist_id}/calendar.json?apikey={API_KEY}'
    res = requests.get(url).json()

    status_ok = res['resultsPage']['status'] == 'ok'
    events_exists = 'event' in res['resultsPage']['results']

    if status_ok and events_exists:
        events = res['resultsPage']['results']['event']

        return events


def get_events_by_ids(artists_ids):
    out = []

    for artist_id in set(artists_ids):
        events = get_events_by_id(artist_id)
        out.append(events)

    return out

