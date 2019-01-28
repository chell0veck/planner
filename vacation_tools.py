import datetime
import itertools
import requests
import os
from pathlib import Path


class Event:

    def __init__(self, artist, artists, display, date, _type, uri, venue, country, city):
        self.artist = artist
        self.artists = artists
        self.display = display
        self.date = date
        self.type = _type
        self.uri = uri
        self.venue = venue
        self.country = country
        self.city = city

    def __repr__(self):
        return '{}'.format(self.display)


def fetch_events(artists):
    _api_key = open(os.path.join(Path(__file__).parents[1], 'songklick_api_key'), 'r').read()
    fetched_events = []

    for artist, artist_id in artists.items():

        url = 'https://api.songkick.com/api/3.0/artists/{}/calendar.json?apikey={}'.format(artist_id, _api_key)
        res = requests.get(url).json()

        if res['resultsPage']['status'] == 'ok':
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

                fetched_events.append(Event(artist, event_artists, event_display, event_date, event_type, event_uri,
                                event_venue, event_country, event_city))

    return fetched_events


class Framer:

    def __init__(self, start, step, holidays=None, events=None):
        self._start = start
        self._end = self._start + datetime.timedelta(step - 1)
        self._events = events if events else ()
        self.holidays = holidays if holidays else ()
        self.duration = (self.end - self.start + datetime.timedelta(1)).days
        self.non_work = len([d for d in self.holidays if self.start <= d <= self.end])
        self.vac = self.duration - self.non_work
        self.efficiency = round(self.non_work/self.duration, 2)

    def match_events(self):
        matches = [event for event in self._events if self.start < event.date < self.end]
        return matches

    def all_events(self):
        all_events = []
        events_all = self.match_events()
        art_num = len(set(event.artist for event in events_all))
        set_all = (itertools.combinations(events_all, i) for i in range(1, art_num+1))

        for events_set in set_all:
            for events in events_set:

                if len(events) == 1:
                    all_events.append(events)

                else:
                    all_evts = len(events)
                    uniq_art = len(set(event.artist for event in events))
                    uniq_dts = len(set(event.date for event in events))

                    if uniq_art == all_evts and uniq_dts == all_evts:
                        all_events.append(events)
        return all_events

    def max_events(self):
        return [events for events in self.all_events() if len(events) == self.events_num]

    def view_events(self):

        pass

    @property
    def start(self):
        start = self._start
        while start - datetime.timedelta(1) in self.holidays:
            start -= datetime.timedelta(1)
        return start

    @property
    def end(self):
        end = self._end
        while end + datetime.timedelta(1) in self.holidays:
            end += datetime.timedelta(1)
        return end

    @property
    def events_num(self):
        all_events = self.all_events()
        events_num = max([len(events) for events in all_events]) if all_events else 0
        return events_num

    def __str__(self):
        return '{} - {}'.format(self.start.strftime('%a %b-%d'), self.end.strftime('%a %b-%d'))