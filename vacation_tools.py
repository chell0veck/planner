import datetime as dt
from sklearn.model_selection import train_test_split
import statsmodels.formula.api as sm
from statsmodels.api import add_constant
import pandas as pd
import itertools


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
        self._events = [Event(event) for event in events] if events else ()
        self.holidays = holidays if holidays else ()
        self.duration = (self.end - self.start + dt.timedelta(1)).days
        self.non_work = len([d for d in self.holidays if self.start <= d <= self.end])
        self.vac = self.duration - self.non_work
        self.efficiency = round(self.non_work/self.duration, 2)

    def match_events(self):
        matches = [event for event in self._events if self.start < event.date < self.end]
        return matches

    def _parse_events(self):
        output=[]
        events_all = self.match_events()
        art_num = len(set(event.artist for event in events_all))
        set_all = (itertools.combinations(events_all, i) for i in range(1, art_num+1))

        for events_set in set_all:
            for events in events_set:

                if len(events) == 1:
                    output.append(events)

                else:
                    all_evts = len(events)
                    uniq_art = len(set(event.artist for event in events))
                    uniq_dts = len(set(event.date for event in events))

                    if uniq_art == all_evts and uniq_dts == all_evts:
                        output.append(events)
        return output

    def parse_events(self):
        return [events for events in self._parse_events() if len(events) == self.events_num]


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

    @property
    def events_num(self):
        all_events = self._parse_events()
        events_num = max([len(events) for events in all_events]) if all_events else 0
        return events_num


    def __str__(self):
        return '{} - {}'.format(self.start.strftime('%a %b-%d'), self.end.strftime('%a %b-%d'))

