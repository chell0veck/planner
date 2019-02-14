import datetime
from vacation_tools import events_framer, events_fetcher
from data_source import nonwork
import pickle


skip = ('Japan', 'New Zealand', 'Australia', 'UK', 'US', 'Canada', 'China')

artists = {'MONO': 201140, 'TOOL': 521019, 'PHIL': 495060,  'CBP': 78386, 'APC':549892, 'Puscifer':594931,
           'Damien Rice':391954, 'Caspian':508722, 'Bell X1': 78581}

raw_events = events_fetcher(artists)
# print(events)

# raw_events = pickle.load(open('events.p', 'rb'))
# # raw_events = events_fetcher(artists)
events = [event for event in raw_events if event.country not in skip]
#
def slice_2019_year():
    all_frames = []

    for day in range(365):
        start = datetime.date(2019, 1, 1) + datetime.timedelta(day)

        for step in range(3, 20):
            frames = events_framer(start, step, nonwork, events)

            all_frames.extend(frames)

    return all_frames
#
#
def test_default_test_model():
    frames = slice_2019_year()
    track = []
    for frame in frames:
        if (frame.start, frame.end) not in track:
            if frame.work_days == 10 and frame.num_events != 0 and frame.efficiency > 0.4:
                print(frame, frame.num_events)
                track.append((frame.start, frame.end))


frames = slice_2019_year()
result = []
duplicated = []

print('    start      end      days   work_days   eff                        events')

for frame in sorted(frames, key=lambda f: f.eff_3):
    if (frame.start, frame.end, sorted(event.city for event in frame.events)) not in duplicated \
            and 'Bell X1' in frame.artists:

        print('{}  {} {:4}     {:4}      {:4}  {:4}   {:4}   {}'.format(frame.start, frame.end, frame.duration, frame.work_days,
                                                             frame.eff_1, frame.eff_2, frame.eff_3, frame.events))
        duplicated.append((frame.start, frame.end, sorted(event.city for event in frame.events)))
