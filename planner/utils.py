""" Supported data types and functions

    Classes:
        Artist
        Day
        Event
        Frame

    Functions:
        timeit
        wrap_events
        wrap_artists
        load_artists
        get_non_work
 """

import datetime
import time
import json

import holidays


from config import ARTISTS


class Artist:
    """
    Artist class holds artist as name and songkick id
    """

    def __init__(self, name, sid):
        self.name = name
        self.sid = sid

    def __repr__(self):
        return f'{self.__class__.__name__}({self.name}, {self.sid})'


class Day:
    """
    To be defined still
    """
    def __init__(self, date, event, nonwork):
        self.date = date
        self.event = event
        self.nonwork = nonwork

    def __repr__(self):
        return f'{self.__class__.__name__}({self.date}, {self.event}, {self.nonwork})'

    def __str__(self):
        return f'{self.date}, {self.event}, {self.nonwork}'


class Event:
    """
    Data type that holds event
    """

    def __init__(self, artist, arts, display, date, event_type, uri, venue, country, city):
        self.artist = artist
        self.artists = arts
        self.display = display
        self.date = date
        self.type = event_type
        self.uri = uri
        self.venue = venue
        self.country = country
        self.city = city

    def __str__(self):
        return f'{self.artist} in {self.city}, {self.country}'

    def __repr__(self):
        return f'{self.__class__.__name__}({self.artist}, {self.artists}, {self.display},' \
               f' {self.date},{self.type}, {self.uri}, {self.venue}, {self.country}, {self.city})'


def timeit(func):
    """
    Maybe not bad implemented timer
    :param func:
    :return:
    """

    def timed():
        time_start = time.time()
        result = func()
        time_end = time.time()
        waisted_seconds = (time_end-time_start) % 60
        print('{} took {:.2} seconds'.format(func.__name__, waisted_seconds))
        return result

    return timed


def wrap_events(events, skip_ctry):
    """
    Wrap events into Event object and filter by the skip counties
    :param events: list
    :param skip_ctry: list
    :return: list
    """
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

    return sorted(result, key=lambda e: e.date)


def wrap_artists(arts):
    """
    Wraps artist loaded from the disk into Artist object
    :param arts: dict(artist_name: artist_id)
    :return: list
    """
    return [Artist(artist, arts[artist]) for artist in arts]


def load_artists(arts=ARTISTS):
    """
    Load artists info from the static
    :param arts: json cache file
    :return: dict
    """

    with open(arts) as static_artists:
        return json.load(static_artists)



def wrap_events_into_days(events, holidays):
    result = []
    visited = []

    for event in events:
        if event.date in holidays:
            result.append(Day(event.date, event, True))
            visited.append(event.date)
        else:
            result.append(Day(event.date, event, False))

    for holiday in holidays:
        if holiday not in visited:
            result.append(Day(holiday, False, True))

    return result



