import datetime as dt


class Event:

    def __init__(self, event):
        self.event = event
        self.artist, self.date, self.geo, self.place = event
        self.city, self.country = self.geo.split(', ')

    def __repr__(self):
        return "Event(('{}', {}, '{}', '{}'))".format(*self.event)


class Planner:

    def __init__(self, start, step, holidays=None, events=None):
        self._start = start
        self._end = self._start + dt.timedelta(step - 1)
        self._events = (Event(event) for event in events) if events else ()
        self.holidays = holidays if holidays else ()
        self.duration = (self.end - self.start + dt.timedelta(1)).days
        self.non_work = len([d for d in self.holidays if self.start <= d <= self.end])
        self.vac = self.duration - self.non_work
        self.efficiency = round(self.non_work/self.duration, 2)

    def match_events(self):
        matches = list((event for event in self._events if self.start < event.date < self.end))
        return len(matches)

    @property
    def start(self):
        start = self._start
        while start - dt.timedelta(1) in self.holidays:
            start -= dt.timedelta(1)
        return start

    @property
    def end(self):
        end = self._end
        while end + dt.timedelta(1) in self.holidays:
            end += dt.timedelta(1)
        return end

    def __str__(self):
        return '{} - {}'.format(self.start.strftime('%a %b-%d'), self.end.strftime('%a %b-%d'))
