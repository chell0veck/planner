import songkick
import static


def default_model():

    events = songkick.load_events()

    for event in sorted(events, key=lambda e: e.date):
        if event.country not in static.SKIP_CTRY\
                and event.date.strftime("%m") in ('10', '11'):
            print(event, event.date.strftime("%A"), event.venue, event.type)


# songkick.dump_events()
#
default_model()
