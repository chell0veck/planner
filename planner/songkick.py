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
import calendarific


holidays = calendarific.load_holidays()
cache = os.path.join(Path(__file__).parents[0], 'static', 'events.pickle')
api_key = open(os.path.join(Path(__file__).parents[0], 'config', '.songkick_api_key'), 'r').read()
artists = json.load(open(os.path.join(Path(__file__).parents[0], 'static', 'artists.json')))


def get_events(artist):
    """ Returns events from songkick for required artist"""

    artist_name, artist_id = artist
    url = f'https://api.songkick.com/api/3.0/artists/{artist_id}/calendar.json?apikey={api_key}'
    res = requests.get(url).json()
    results = []

    status_ok = res['resultsPage']['status'] == 'ok'
    events_exists = 'event' in res['resultsPage']['results']

    if status_ok and events_exists:
        events = res['resultsPage']['results']['event']

        for event in events:
            event_artists = [e['displayName'] for e in event['performance']]
            event_display = event['displayName']
            event_date = datetime.datetime.strptime(event['start']['date'], '%Y-%m-%d').date()
            event_type = event['type']
            event_uri = event['uri']
            event_venue = event['venue']['displayName']
            event_country = event['venue']['metroArea']['country']['displayName']
            event_city = event['venue']['metroArea']['displayName']

            results.append(Event(artist_name, event_artists, event_display, event_date, event_type,
                                 event_uri, event_venue, event_country, event_city))

    return results


def dump_events(artists=artists):
    """ Dump events on dist"""
    results = []

    for artist in artists.items():
        events = get_events(artist)
        results.extend(events)

    for holiday in holidays:
        if holiday > datetime.date.today():
            event = Event('Holiday', 'Holiday', 'Holiday', holiday, 'Holiday',
                          'Holiday', 'Holiday', 'Holiday', 'Ukraine')
            results.append(event)

    with open(cache, 'wb') as f:
        pickle.dump(results, f)


def load_events():
    """ Load events from disk"""

    with open(cache, 'rb') as f:
        return pickle.load(f)


def get_events_by_artist_id(artist_id):
    url = f'https://api.songkick.com/api/3.0/artists/{artist_id}/calendar.json?apikey={api_key}'
    res = requests.get(url).json()

    status_ok = res['resultsPage']['status'] == 'ok'
    events_exists = 'event' in res['resultsPage']['results']

    if status_ok and events_exists:
        events = res['resultsPage']['results']['event']

        return events


print(get_events_by_artist_id(("Mono", 201140)))

