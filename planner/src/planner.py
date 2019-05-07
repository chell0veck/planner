import datetime

import songkick
import data


events = songkick.load_events()

for event in events:
    if event.country not in data.SKIP_CTRY\
            and event.type == 'Concert'\
            and event.date.weekday() in (4, 5, 6):
        print(event, event.date.strftime("%A"))
