"""Create songkick API interface.

Functions:
    fetch_artist
    fetch_artists

"""
import datetime
import requests
import json

from utils import wrap_artists, wrap_events


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


def load_events():

    if _cache_is_stale():
        refresh_cache()

    events = load_cache()
    return events


def refresh_cache():
    raw_artists = json.load(open('_static_artists.json'))
    fmt_artists = wrap_artists(raw_artists)
    raw_events = get_events(fmt_artists)
    dump_cache(raw_events)


def dump_cache(obj):
    timestamp = datetime.datetime.now()

    with open(cache, 'w') as fp:
        json.dump(obj, fp)

    with open('_static_events.time','w') as cache_time:
        cache_time.write(str(timestamp))


def load_cache():
    skip_ctrys = json.load(open('_static_skip_ctry.json'))

    with open(cache, 'r') as fp:
        raw_events = json.load(fp)

    fmt_events = wrap_events(raw_events, skip_ctrys)
    return fmt_events


def _validate_data(data):
    response_ok = data['resultsPage']['status'] == 'ok'
    events_exist = 'event' in data['resultsPage']['results']
    return response_ok and events_exist


def _cache_is_stale():
    cache_file = '_static_events.time'
    cache_raw_time = open(cache_file, 'r').read()
    cache_time = datetime.datetime.fromisoformat(cache_raw_time)
    print(cache_time)
    # current_time = datetime.datetime.now().timestamp()
    # cache_age = current_time - cache_time
    # cache_is_stale = True if cache_age > 1 else False
    # return cache_is_stale
