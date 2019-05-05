from planner.vacation_tools import events_fetcher, slice_this_year
from planner.data_source import nonwork, skip_countries, artists


def test_model():
    events = [event for event in events_fetcher(artists) if event.country not in skip_countries]
    frames = slice_this_year(nonwork, events)
    duplicated = []

    print('    start      end      days   work_days   eff                        events')

    for frame in sorted(frames, key=lambda f: f.eff):
        if (frame.start, frame.end, sorted(event.city for event in frame.events)) not in duplicated\
                and 'TOOL' in frame.artists and 'Florence' in frame.cities:
                # and 'Florence' in frame.cities and frame.n_artists == 1:

            print('{}  {} {:4}   {:4}        {:4}   {}'.format(frame.start, frame.end, frame.duration,
                                                                            frame.work_days, frame.eff, frame.events))

            duplicated.append((frame.start, frame.end, sorted(event.city for event in frame.events)))


# test_model()

