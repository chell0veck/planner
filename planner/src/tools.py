import datetime
import itertools
import requests
import os
from pathlib import Path
import pickle


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
        return '{}, {}, {}'.format(self.artist, self.date, self.city, self.country)


class Frame:

    def __init__(self, start, end, events, holidays):
        self.start = start
        self.end = end

        self.nonwork_days = len(holidays)
        self.duration = (end - start + datetime.timedelta(1)).days
        self.work_days = self.duration - self.nonwork_days

        self.holidays = holidays
        self.events = events
        self.cities = set(event.city for event in self.events)
        self.artists = set(event.artist for event in self.events)
        self.countries = set(event.country for event in self.events)

        self.n_holidays = len(self.holidays)
        self.n_events = len(self.events)
        self.n_cities = len(self.cities)
        self.n_artists = len(self.artists)
        self.n_countries = len(self.countries)

        self.eff = round(self.nonwork_days / self.duration, 2)

    def view_frame(self):
        return [(event.artist, event.country) for event in self.events]

    def __str__(self):
        return '{} - {}, days:{:2}  work:{:2} efficiency:{:2}'.format(self.start.strftime('%a %d %b'),
                                                                      self.end.strftime('%a %d %b'),
                                                                      self.duration, self.work_days,
                                                                      self.eff)


def events_fetcher(artists):
    _api_key = open(os.path.join(Path(__file__).parents[1], 'resources','.SNK_API_KEY.txt'), 'r').read()
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


def this_year_artists(artists):
    events = events_fetcher(artists)
    print(set([event.artist for event in events]))


def slice_this_year(nonwork, events):
    all_frames = []

    for day in range(365):
        start = datetime.date(2019, 1, 1) + datetime.timedelta(day)

        for step in range(3, 20):
            frames = events_framer(start, step, nonwork, events)

            all_frames.extend(frames)

    return all_frames


def songkick_get_events(artist):
    events = []
    _api_key = open(os.path.join(Path(__file__).parents[1], 'resources', '.SNK_API_KEY.txt'), 'r').read()

    for artist_name, artist_id in artist.items():
        url = 'https://api.songkick.com/api/3.0/artists/{}/calendar.json?apikey={}'.format(artist_id, _api_key)
        res = requests.get(url).json()

        if res['resultsPage']['status'] == 'ok' and 'event' in res['resultsPage']['results']:
            _events = res['resultsPage']['results']['event']

            for _event in _events:
                _event_artists = [e['displayName'] for e in _event['performance']]
                _event_display = _event['displayName']
                _event_date = datetime.datetime.strptime(_event['start']['date'], '%Y-%m-%d').date()
                _event_type = _event['type']
                _event_uri = _event['uri']
                _event_venue = _event['venue']['displayName']
                _event_country = _event['venue']['metroArea']['country']['displayName']
                _event_city = _event['venue']['metroArea']['displayName']

                events.append(Event(artist_name, _event_artists, _event_display, _event_date, _event_type, _event_uri,
                                    _event_venue, _event_country, _event_city))

    return events


def songkick_dump_events(artists, file=os.path.join(Path(__file__).parents[1], 'resources','events.pickle')):
    results = []

    for artist in artists.items():
        print(artist)
        # events = songkick_get_events(artist)
        # print(events)
        # results.extend(events)
    #
    # print(results)
    #
    # with open(file) as f:
    #     pickle.dump(results,f)


print(songkick_get_events({'Mono': 201140}))
songkick_dump_events({'Mono': 201140, 'Tool': 521019})
