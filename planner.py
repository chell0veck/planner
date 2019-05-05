from data_src import ARTISTS
from tools import events_fetcher
import pickle

events = pickle.load(open('events.pickle','rb'))

results = [[event.artist, event.date, event.city] for event in events]
results.sort(key=lambda e: e[1])

for event in results:
    print('{:12} {:22} {}'.format(event[0], event[1].strftime('%d %B %A'), event[2]))
