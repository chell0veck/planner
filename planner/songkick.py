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


def fetch_artist(artist):
    url = _build_url(artist)
    data = requests.get(url).json()
    data_valid = _validate_response(data)

    if data_valid:
        events = data['resultsPage']['results']['event']
        return [(artist.name, event) for event in events]


def fetch_artists(artists):
    out = []

    for artist in artists:
        events = fetch_artist(artist)
        out.append(events)

    return out


def _build_url(artist, token=api_key):
    url = url_tml.format(artist.sid, token)
    return url


def _validate_response(data):
    response_ok = data['resultsPage']['status'] == 'ok'
    events_exist = 'event' in data['resultsPage']['results']
    return response_ok and events_exist


def dump_cache(obj):
    with open(cache) as fp:
        json.dump(obj, fp)


def load_cache():
    with open(cache) as fp:
        return json.load(fp)
