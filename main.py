import songkick
import static
import calendarific
import pickle


song_api = songkick.API()


def default_model():

    events = song_api.load_cache()

    for event in sorted(events, key=lambda e: e.date):
        if event.country not in static.SKIP_CTRY\
                and event.date.strftime("%m") in ('10', '11'):
            print(event, event.date.strftime("%A"), event.venue, event.type)


song_api.dump_cache()

default_model()

