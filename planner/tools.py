""" Additional datatypes.

    Classes:

    Event
    Frame

 """

import datetime
import time



class Event:

    def __init__(self, artist, artists, display, date, event_type, uri, venue, country, city):
        self.artist = artist
        self.artists = artists
        self.display = display
        self.date = date
        self.type = event_type
        self.uri = uri
        self.venue = venue
        self.country = country
        self.city = city

    def __repr__(self):
        return '{:15} {} {:10} {:20} {}'\
            .format(self.artist, self.date, self.date.strftime("%A"), self.city, self.country)


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


def timeit(method):

    def timed(*args):
        ts = time.time()
        result = method(*args)
        te = time.time()
        ws = (te-ts) % 60
        print('{}({}) took {:.2} seconds'.format(method.__name__, *args, ws))
        return result

    return timed


def wrap_events(artist_name, events):
    results = []

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


def fetch_artists_id(artists):
    return artists.keys()

from static import artists
print(artists)