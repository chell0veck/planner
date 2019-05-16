import timetable
import songkick
import json


from tools import Event, Date, wrap_events


def default_model():
    result = []
    raw_events = songkick.load_events()
    fmt_events = wrap_events(raw_events)
    nonwork = timetable.get_nonwork()

    for event in fmt_events:
        if event.date in nonwork:
            result.append(Date(event.date, event, True))
        result.append(Date(event.date, event, False))

    return result


print(default_model())


