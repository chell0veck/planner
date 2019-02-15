from vacation_tools import events_framer, events_fetcher, slice_this_year, this_year_artists
from data_source import nonwork, skip, artists


def test_model():
    events = [event for event in events_fetcher(artists) if event.country not in skip]
    frames = slice_this_year(nonwork, events)
    duplicated = []

    print('    start      end      days   work_days   eff                        events')

    for frame in sorted(frames, key=lambda f: f.eff_3):
        if (frame.start, frame.end, sorted(event.city for event in frame.events)) not in duplicated \
                and frame.n_artists == 0:

            print('{}  {} {:4}     {:4}      {:4}  {:4}   {:4}   {}'.format(frame.start, frame.end, frame.duration,
                                                                            frame.work_days,frame.eff_1, frame.eff_2,
                                                                            frame.eff_3, frame.events))
            duplicated.append((frame.start, frame.end, sorted(event.city for event in frame.events)))


test_model()
