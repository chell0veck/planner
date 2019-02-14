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
        return '{}, {}, {}'.format(self.artist, self.date, self.city)


class Frame:

    def __init__(self, start, end, events, holidays):
        self.start = start
        self.end = end
        self.events = events
        self.holidays = holidays
        self.nonwork_days = len(holidays)
        self.num_events = len(events)
        self.duration = (end - start + datetime.timedelta(1)).days
        self.work_days = self.duration - self.nonwork_days
        self.efficiency = round(self.nonwork_days/self.duration, 2)
        self.comp_eff_1 = round((self.efficiency * 0.5 + self.num_events * 0.1), 2)
        self.n_artists = len(set(event.artist for event in self.events))
        # self.comp_eff_2 = round((self.efficiency * 0.4 + self.num_events / self.unique_artists * 0.6), 2)\
        #                     if self.events else self.comp_eff_1
        # self.comp_eff_2 = round((self.efficiency * 0.1 + self.num_events / self.n_artists * 0.2), 2)\
        #                     if self.events else self.comp_eff_1

        self.eff_1 = round(self.nonwork_days/self.duration, 2)
        self.eff_2 = round((self.num_events/5),2 ) if self.events else self.eff_1
        self.eff_3 = round(self.eff_1 + self.eff_2, 2)

        self.cities = set(event.city for event in self.events)
        self.n_cities = len(self.cities)
        self.countries = set(event.country for event in self.events)
        self.n_countries = len(self.countries)
        self.artists = set(event.artist for event in self.events)
        self.n_artists = len(self.artists)

    def view_events(self):
        return [(event.artist, event.country) for event in self.events]

    def __str__(self):
        return '{} - {}, days:{:2}  work:{:2} efficiency:{:2}'.format(self.start.strftime('%a %d %b'), self.end.strftime('%a %d %b'),
                                         self.duration, self.work_days, self.efficiency)


def events_fetcher(artists):
    _api_key = open(os.path.join(Path(__file__).parents[1], 'songklick_api_key'), 'r').read()
    fetched_events = []

    for artist, artist_id in artists.items():

        url = 'https://api.songkick.com/api/3.0/artists/{}/calendar.json?apikey={}'.format(artist_id, _api_key)
        res = requests.get(url).json()

        if res['resultsPage']['status'] == 'ok':
            if 'event' in res['resultsPage']['results']:
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


def events_framer(start, step, holidays, events=None):
    all_frames = []
    end = start + datetime.timedelta(step - 1)

    while end + datetime.timedelta(1) in holidays:
        end += datetime.timedelta(1)

    while start - datetime.timedelta(1) in holidays:
        start -= datetime.timedelta(1)

    nonworking_days = set(day for day in holidays if start <= day <= end)

    if events:
        events_matches = [event for event in events if start < event.date < end]
        artists_number = len(set(event.artist for event in events_matches))
        events_combo = [itertools.combinations(events_matches, i) for i in range(1, artists_number+1)]

        for events_set in events_combo:
            for events in events_set:

                if len(events) == 1:
                    all_frames.append(Frame(start, end, events, nonworking_days))

                else:
                    all_evts = len(events)
                    uniq_art = len(set(event.artist for event in events))
                    uniq_dts = len(set(event.date for event in events))

                    if uniq_art == all_evts and uniq_dts == all_evts:
                        all_frames.append(Frame(start, end, events, nonworking_days))

    all_frames.append(Frame(start, end, [], nonworking_days))

    return all_frames
