import os
from pathlib import Path
import pickle


FILE = os.path.join(Path(__file__).parents[1], 'resources','events.pickle')

events = pickle.load(open(FILE, 'rb'))

results = [[event.artist, event.date, event.city] for event in events]
results.sort(key=lambda e: e[1])

for event in results:
    print('{:12} {:22} {}'.format(event[0], event[1].strftime('%d %B %A'), event[2]))
