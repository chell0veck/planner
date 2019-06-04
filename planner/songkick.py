""" Songkick API interface.
From my understanding supports only Event JSON official response object from api call.
Main usage is get_events.
It returns events from the cache and if cache is stale update it before that.

Functions:
    get_events
    load_events
    refresh_cache
    dump_cache
    load_cache

System functions:
    _response_is_valid
    _cache_is_stale
"""

import datetime
import json

import requests

from data_utils import wrap_artists, wrap_events
from config import SGK_API_URL, SGK_API_KEY, SKIP_COUNTRIES, ARTISTS, CACHE_DATA, CACHE_TIME


def get_events(artists):
    """
    Return a list of [artist.name, artist.events] objects
    received from songkick api for passed Artist or list(Artist)

    :param artists: Event object or list of Event objects
    :return: list
    """

    out = []

    for artist in artists:
        url = SGK_API_URL.format(artist.sid, SGK_API_KEY)
        data = requests.get(url).json()
        data_valid = _response_is_valid(data)

        if data_valid:
            events = data['resultsPage']['results']['event']
            wrapped = [[artist.name, event] for event in events]
            out.extend(wrapped)

    return out


def load_events():
    """ Return list of events from the cache wrapped in Event.

    Additional actions:
    - skip events that happen in countries to skip;
    - update the cache if it's been updated more that 24 hours ago;

    :return: list
    """
    skip = json.load(open(SKIP_COUNTRIES))

    cache_is_stale = _cache_is_stale()

    if cache_is_stale:
        refresh_cache()

    raw_events = load_cache()
    fmt_events = wrap_events(raw_events, skip)

    return fmt_events


def refresh_cache():
    """
    Refresh the cache.
    """
    raw_artists = json.load(open(ARTISTS))
    fmt_artists = wrap_artists(raw_artists)
    raw_events = get_events(fmt_artists)
    dump_cache(raw_events)


def dump_cache(obj):
    """
    Serialize cache into disk in json and save cache update timestamp in UTC.

    :param obj: cache (output or get_events)
    :return: None
    """
    timestamp = datetime.datetime.now()

    with open(CACHE_DATA, 'w') as c_d:
        json.dump(obj, c_d)

    with open(CACHE_TIME, 'w') as c_t:
        c_t.write(str(timestamp.utcnow()))


def load_cache():
    """
    Return events loaded from the cache

    :return: list
    """

    with open(CACHE_DATA) as c_d:
        return json.load(c_d)


def _response_is_valid(data):
    """
    Check if songkick api response is valid

    :param data: json # (request.get().json())
    :return: bool
    """
    response_ok = data['resultsPage']['status'] == 'ok'
    events_exist = 'event' in data['resultsPage']['results']
    return response_ok and events_exist


def _cache_is_stale():
    """
    Check if cache been updated more than 24 hours ago

    :return: bool
    """
    cache_utc_time = datetime.datetime.strptime(open(CACHE_TIME, 'r').read(),
                                                '%Y-%m-%d %H:%M:%S.%f')
    curr_utc_time = datetime.datetime.utcnow()

    diff = curr_utc_time - cache_utc_time

    if diff.days >= 1:
        return True

    return False
