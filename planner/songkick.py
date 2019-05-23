"""Create songkick API interface.

Functions:
    fetch_artist
    fetch_artists

"""

import datetime
import requests
import json

from utils import wrap_artists, wrap_events
import utils


url_tml = 'https://api.songkick.com/api/3.0/artists/{}/calendar.json?apikey={}'
api_key = open('.songkick_api_key', 'r').read()
skip_ctrys = '_static_skip_ctry.json'
cache_data = '_static_events.json'
cache_time = '_static_events.time'
artists = '_static_artists.json'


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


def load_events():
    skip = json.load(open(skip_ctrys))

    cache_is_stale = check_cache()

    if cache_is_stale:
        refresh_cache()

    raw_events = load_cache()
    fmt_events = wrap_events(raw_events, skip)

    return fmt_events


def refresh_cache():
    raw_artists = json.load(open(artists))
    fmt_artists = wrap_artists(raw_artists)
    raw_events = get_events(fmt_artists)
    dump_cache(raw_events)


def dump_cache(obj):
    timestamp = datetime.datetime.now()

    with open(cache_data, 'w') as fp:
        json.dump(obj, fp)

    with open('_static_events.time', 'w') as cache_time:
        cache_time.write(str(timestamp))


def load_cache():

    with open(cache_data) as c:
        return json.load(c)


def _validate_data(data):
    response_ok = data['resultsPage']['status'] == 'ok'
    events_exist = 'event' in data['resultsPage']['results']
    return response_ok and events_exist


def check_cache():
    ctime = datetime.datetime.fromisoformat(open(cache_time, 'r').read())
    now = datetime.datetime.now()
    diff = now - ctime

    if diff.days >= 1:
        return True

    return False



