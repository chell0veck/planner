import datetime as dt
from sklearn.model_selection import train_test_split
import statsmodels.formula.api as sm
from statsmodels.api import add_constant
import pandas as pd


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

        return matches

    def get_prediction(self):
        pass


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


class Predictor:

    def __init__(self, vacation, duration, events):
        self.vacation = vacation
        self.duration = duration
        self.events = events

    def predict(self):
        dataset = pd.read_excel('learn_dataset.xlsx', index_col=0, header=0)
        X = dataset.iloc[:, :-1].values
        y = dataset.iloc[:, -1:].values
        X = add_constant(X)
        ols_reg = sm.OLS(y, X).fit()
        prediction = ols_reg.predict([[1, self.vacation, self.duration, self.events]])
        return round(*prediction, 2)
