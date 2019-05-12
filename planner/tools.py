""" Additional datatypes.

    Classes:

    Event
    Frame

 """

import datetime


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
        return '{:15} {} {:20} {}'.format(self.artist, self.date, self.city, self.country)


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
