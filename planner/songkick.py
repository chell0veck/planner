"""Create songkick API interface.

Functions:
    fetch_artist
    fetch_artists

"""

import requests
import json


url_tml = 'https://api.songkick.com/api/3.0/artists/{}/calendar.json?apikey={}'
api_key = open('.songkick_api_key', 'r').read()
cache = '_static_events.json'


def get_events(artists):
    out = []

    for artist in artists:
        url = url_tml.format(artist.sid, api_key)
        data = requests.get(url).json()
        data_valid = _validate_data(data)

        if data_valid:
            events = data['resultsPage']['results']['event']
            wrapped = [[artist.name, event] for event in events]
            out.extend(wrapped)

    return out


def dump_cache(obj):
    with open(cache, 'w') as fp:
        json.dump(obj, fp)


def load_cache():
    with open(cache, 'r') as fp:
        return json.load(fp)


def _validate_data(data):
    response_ok = data['resultsPage']['status'] == 'ok'
    events_exist = 'event' in data['resultsPage']['results']
    return response_ok and events_exist

