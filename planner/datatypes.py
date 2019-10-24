class Event:

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
        return f'{self.date} - {self.artist} in {self.city}, {self.country}'

    def __repr__(self):
        return f'{self.__class__.__name__}({self.artist}, {self.artists}, {self.display},' \
               f' {self.date},{self.type}, {self.uri}, {self.venue}, {self.country}, {self.city})'
