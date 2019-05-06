import os
from pathlib import Path
import pickle


FILE = os.path.join(Path(__file__).parents[1], 'resources','events.pickle')

events = pickle.load(open(FILE, 'rb'))

results = [[event.artist, event.date, event.city, event.country] for event in events]
results.sort(key=lambda e: e[1])

for event in results:
    evnt = '{:12} {:22} {:20} {:20}'.format(event[0], event[1].strftime('%d %B %A'), event[2], event[3])
    coutry = event[3]
    if coutry != 'US':
        print(evnt)
