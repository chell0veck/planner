import datetime

import songkick
import static

# songkick.dump_events()

events = songkick.load_events()


for event in events:
    if event.country not in static.SKIP_CTRY\
            and event.type == 'Concert'\
            and event.date.weekday() in (4, 5, 6):
        print(event, event.date.strftime("%A"))


