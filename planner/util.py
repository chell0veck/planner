""" Additional datatypes.

    Classes:

    Event
    Frame

 """

import datetime
import time


class Day:
    def __init__(self, date, event, nonwork):
        self.date = date
        self.event = event
        self.nonwork = nonwork

    def __repr__(self):
        return f'{self.__class__.__name__}({self.date}, {self.event}, {self.nonwork})'


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

    def __str__(self):
        return f'{self.artist} at {self.city}'

    def __repr__(self):
        return f'Event({self.artist}, {self.artists}, {self.display}, {self.date},' \
               f' {self.type}, {self.uri}, {self.venue}, {self.country}, {self.city})'


class Frame:

    def __init__(self, start, end, events, holidays):
        self.start = start
        self.end = end


class Artist:

    def __init__(self, name, sid):
        self.name = name
        self.sid = sid

    def __repr__(self):
        return f'{self.__class__.__name__}({self.name}, {self.sid})'


def timeit(method):

    def timed(*args):
        ts = time.time()
        result = method(*args)
        te = time.time()
        ws = (te-ts) % 60
        print('{}({}) took {:.2} seconds'.format(method.__name__, *args, ws))
        return result

    return timed


def wrap_events(events, skip_ctry):
        result = []

        for event in events:
            artist, details = event
            event_artists = [e['displayName'] for e in details['performance']]
            event_display = details['displayName']
            event_date = datetime.datetime.strptime(details['start']['date'], '%Y-%m-%d').date()
            event_type = details['type']
            event_uri = details['uri']
            event_venue = details['venue']['displayName']
            event_country = details['venue']['metroArea']['country']['displayName']
            event_city = details['venue']['metroArea']['displayName']

            if event_country not in skip_ctry:

                result.append(Event(artist, event_artists, event_display, event_date, event_type,
                                    event_uri, event_venue, event_country, event_city))

        return result
