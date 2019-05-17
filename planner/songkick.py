"""Create songkick API interface.

Functions:

    get_events(tuple) -> list
    dump_events(dict) -> serialing to ../resources/songkick_events.pickle
    load_events(file) -> object

"""


import requests
import json

from tools import Artist


class Api:

    def __init__(self, artist):
        self.api_key = open('.songkick_api_key', 'r').read()
        self.url_tml = 'https://api.songkick.com/api/3.0/artists/{}/calendar.json?apikey={}'
        self.cache = '_static_events.json'
        self.artist = artist

    @property
    def url(self):
        url = self.url_tml.format(self.artist.sid, self.api_key)
        return url

    @property
    def data(self):
        url = self.url
        data = requests.get(url).json()
        return data

    @property
    def valid_data(self):
        data = self.data
        status_ok = data['resultsPage']['status'] == 'ok'
        events_exist = 'event' in data['resultsPage']['results']
        return status_ok and events_exist

    def get_events(self):
        if self.valid_data:
            events = self.data['resultsPage']['results']['event']
            return [(self.artist.name, event) for event in events]

    def __repr__(self):
        return f'{self.__class__.__name__}({self.artist})'


arts = Artist('Mono', 201140)
sng_in = Api(arts)


print(sng_in.get_events())
