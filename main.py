import json
import os
from pathlib import Path

import songkick
from static import events, skip_ctry


def default_model():

    for event in sorted(events, key=lambda e: e.date):
        if event.country not in skip_ctry\
                and event.type == 'Concert':
            print(event, event.date.strftime("%A"), event.country)


default_model()
