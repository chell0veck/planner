from datetime import datetime, timedelta


class Event:

    def __init__(self, artist, artists, display, date, type, uri, venue, country, city):
        self.artist = artist
        self.artists = artists
        self.display = display
        self.date = datetime.strptime(date, '%Y-%m-%d')
        self.type = type
        self.uri = uri
        self.venue = venue
        self.country = country
        self.city = city
        self.month = self.date.month

    def __str__(self):
        return f'{self.date.date()} - {self.artist} in {self.city}, {self.country}'

    def __repr__(self):
        return f'{self.__class__.__name__}({self.artist}, {self.artists}, {self.display},' \
               f' {self.date},{self.type}, {self.uri}, {self.venue}, {self.country}, {self.city})'


class EventProcessor:
    def __init__(self, events):
        self.events = sorted(events, key=lambda event: event.date)
        self.str_date = self.events[0].date
        self.end_date = self.events[-1].date
        self.events_num = len(self.events)
        self.full_period = (self.end_date - self.str_date).days

    def process(self, window=20):
        events = self._get_events(self.events, window)
        for event in events:
            print(event)

    @staticmethod
    def _get_events(events, window):
        first_event = events[0]
        result = []
        for event in events[1:]:
            if event.date - first_event.date <= timedelta(days=window):
                result.append(event)
        return result




