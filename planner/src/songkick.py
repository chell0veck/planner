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

from pathlib import Path

from tools import Event
from static import ARTISTS


class API:

    def __init__(self):
        self.cache = os.path.join(Path(__file__).parents[1], 'resources', 'songkick_events.pickle')
        self.api_key = open(os.path.join(Path(__file__).parents[1], 'resources', '.songkick_api_key'), 'r').read()

    def get_events(self, artist):
        """ Returns events from songkick for required artist"""

        artist_name, artist_id = artist
        url = 'https://api.songkick.com/api/3.0/artists/{}/calendar.json?apikey={}'.format(artist_id, self.api_key)
        response = requests.get(url).json()
        results = []

        status_ok = response['resultsPage']['status'] == 'ok'
        events_exists = 'event' in response['resultsPage']['results']

        if status_ok and events_exists:
            events = response['resultsPage']['results']['event']

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

    def dump_cache(self, artists=ARTISTS):
        """Cache events"""

        results = []

        for artist in artists.items():
            events = self.get_events(artist)
            results.extend(events)

        with open(self.cache, 'wb') as f:
            pickle.dump(results, f)

    def load_cache(self, artists=ARTISTS):
        """Load events from cache"""

        with open(self.cache, 'rb') as f:
            return pickle.load(f)
