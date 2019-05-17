import json

import timetable
import songkick
import tools


skip_ctry = json.load(open('_static_skip_ctry.json', 'r'))


def all_events():
    result = []
    raw_events = songkick.load_events()
    fmt_events = tools.wrap_events(raw_events, skip_ctry)
    nonwork = timetable.get_nonwork()

    for event in fmt_events:
        if event.date in nonwork:
            result.append(tools.Day(event.date, event, True))
        result.append(tools.Day(event.date, event, False))

    return result


artists = json.load(open('_static_artists.json', 'r'))
# print(artists)
events = songkick.Api(artists)
print(events.load_cache())