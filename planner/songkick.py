"""Create songkick API interface.

Functions:

    get_events(tuple) -> list
    dump_events(dict) -> serialing to ../resources/songkick_events.pickle
    load_events(file) -> object

"""


import requests
import json

API_KEY = open('.songkick_api_key', 'r').read()
CACHE = '_static_events.json'


def get_events(artists):
    result = []

    for artist_name, artist_id in artists.items():
        url = f'https://api.songkick.com/api/3.0/artists/{artist_id}/calendar.json?apikey={API_KEY}'
        res = requests.get(url).json()

        status_ok = res['resultsPage']['status'] == 'ok'
        events_exists = 'event' in res['resultsPage']['results']

        if status_ok and events_exists:
            events = res['resultsPage']['results']['event']
            result.append((artist_name, events))

    return result


def dump_events(events, f=CACHE):
    with open(f, 'w') as f:
        json.dump(events, f)


def load_events(events=CACHE):
    with open(events, 'r') as events:
        return json.load(events)
