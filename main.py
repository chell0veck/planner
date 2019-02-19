from vacation_tools import events_framer, events_fetcher, slice_this_year, this_year_artists
from data_source import nonwork, skip, artists
import datetime


def test_model():
    events = [event for event in events_fetcher(artists) if event.country not in skip]
    frames = slice_this_year(nonwork, events)
    duplicated = []

    print('    start      end      days   work_days   eff                        events')

    for frame in sorted(frames, key=lambda f: f.eff):
        if (frame.start, frame.end, sorted(event.city for event in frame.events)) not in duplicated\
                and 'Florence' in frame.cities and frame.n_artists == 1 and frame.duration > 9:

            print('{}  {} {:4}     {:4}      {}'.format(frame.start, frame.end, frame.duration,
                                                                            frame.work_days, frame.eff, frame.events))

            duplicated.append((frame.start, frame.end, sorted(event.city for event in frame.events)))


test_model()
