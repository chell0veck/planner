import json
import os
from pathlib import Path

import songkick
import calendarific
from static import events, skip_ctry, artists


def default_model():

    for event in sorted(events, key=lambda e: e.date):
        if event.country not in skip_ctry\
                and event.type in ('Concert', 'Holiday'):
            print(event)


# calendarific.dump_holidays()
# songkick.dump_events()
# default_model()

songkick.dump_events(artists)


