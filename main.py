import songkick
import static


def default_model():

    events = songkick.load_events()

    for event in events:
        if event.country == 'Russia':
            print(event, event.date.strftime("%A"))


default_model()