import json
import songkick as sgk

from utils import Frame, wrap_events, wrap_artists


def refresh_cache():
    raw_artists = json.load(open('_static_artists.json'))
    fmt_artists = wrap_artists(raw_artists)
    raw_events = sgk.get_events(fmt_artists)
    sgk.dump_cache(raw_events)


def load_cache():
    skip_ctrys = json.load(open('_static_skip_ctry.json'))
    raw_events = sgk.load_cache()
    fmt_events = wrap_events(raw_events, skip_ctrys)
    return fmt_events


# refresh_cache()
events = load_cache()

for event in events:
    if event.date.month in (5, 6):
        print(event)
