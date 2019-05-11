import songkick
import static


def default_model():

    events = songkick.load_events()

    for event in sorted(events, key=lambda e: e.date):
        if event.country not in static.SKIP_CTRY\
                and event.country == 'Ireland':
            print(event, event.date.strftime("%A"))


default_model()
