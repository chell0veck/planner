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
        get_nonwork
 """

import datetime
import time
import json

import holidays
from config import artists, skip_countries


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


class Event:
    """
    Data type that holds event
    """

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
        return f'{self.date}, {self.artist} in {self.city}, {self.country}'

    def __repr__(self):
        return f'{self.__class__.__name__}({self.artist}, {self.artists}, {self.display},' \
               f' {self.date},{self.type}, {self.uri}, {self.venue}, {self.country}, {self.city})'


class Frame:
    """
    To be defined still
    """

    def __init__(self, year):
        self.start = datetime.date(year, 1, 1)
        self.end = datetime.date(year, 12, 31)
        self.nonwk = get_nonwork(year)
        # self.raw_events =


def timeit(func):
    """
    Maybe not bad implemented timer
    :param func:
    :return:
    """

    def timed():
        ts = time.time()
        result = func()
        te = time.time()
        ws = (te-ts) % 60
        print('{} took {:.2} seconds'.format(func.__name__, ws))
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


def wrap_artists(artists):
    """
    Wraps artist loaded from the disk into Artist object
    :param artists: dict(artist_name: artist_id)
    :return: list
    """
    return [Artist(artist, artists[artist]) for artist in artists]


def load_artists(arts=artists):
    """
    Load artists info from the static
    :param arts: json cache file
    :return: dict
    """

    with open(arts, 'r') as fp:
        return json.load(fp)


def get_nonwork(year=datetime.datetime.today().year):
    """
    To be defined
    :param year:
    :return:
    """
    _holidays = [dt for dt in holidays.UA(years=year)]
    first_day = datetime.date(year, 1, 1)
    weekdays = [(first_day + datetime.timedelta(i)) for i in range(370)
                if (first_day + datetime.timedelta(i)).weekday() in (5, 6)
                and (first_day + datetime.timedelta(i)).year == year]
    non_working_days = _holidays + weekdays

    return sorted(non_working_days)
