import timetable
import songkick
import tools


def default_model():
    result = []
    raw_events = songkick.load_events()
    fmt_events = tools.wrap_events(raw_events)
    nonwork = timetable.get_nonwork()

    for event in fmt_events:
        if event.date in nonwork:
            result.append(tools.Date(event.date, event, True))
        result.append(tools.Date(event.date, event, False))

    return result


print(default_model())


