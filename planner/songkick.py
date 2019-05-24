"""Create songkick API interface.

Functions:
    fetch_artist
    fetch_artists

"""

import datetime
import requests
import json

from utils import wrap_artists, wrap_events
from config import sgk_api_url, sgk_api_key, skip_ctrys, artists, cache_data, cache_time


def get_events(artists):
    out = []

    for artist in artists:
        url = sgk_api_url.format(artist.sid, sgk_api_key)
        data = requests.get(url).json()
        data_valid = _validate_data(data)

        if data_valid:
            events = data['resultsPage']['results']['event']
            wrapped = [[artist.name, event] for event in events]
            out.extend(wrapped)

    return out


def load_events():
    skip = json.load(open(skip_ctrys))

    cache_is_stale = _check_cache()

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

    with open(cache_data, 'w') as cd:
        json.dump(obj, cd)

    with open(cache_time, 'w') as ct:
        ct.write(str(timestamp.astimezone()))


def load_cache():

    with open(cache_data) as c:
        return json.load(c)


def _validate_data(data):
    response_ok = data['resultsPage']['status'] == 'ok'
    events_exist = 'event' in data['resultsPage']['results']
    return response_ok and events_exist


def _check_cache():
    ctime = datetime.datetime.fromisoformat(open(cache_time, 'r').read())
    now = datetime.datetime.now().astimezone()
    diff = now - ctime

    if diff.days >= 1:
        return True

    return False


events = load_events()
for event in events:
    print(event)

