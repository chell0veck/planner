import datetime
import matplotlib.pyplot as plt

from vacation_tools import events_framer
from data_source import nonwork
import pickle
import time

import pandas as pd

skip = ('Japan', 'New Zealand', 'Australia', 'UK', 'US', 'Canada', 'China')

artists = {'MONO': 201140, 'TOOL': 521019, 'PHIL': 495060,  'CBP': 78386}
raw_events = pickle.load(open('events.p', 'rb'))
events = [event for event in raw_events if event.country not in skip]


def slice_2019_year():
    all_frames = []
    track = []

    for day in range(365):
        start = datetime.date(2019, 1, 1) + datetime.timedelta(day)

        for step in range(3, 20):
            frames = events_framer(start, step, nonwork, events)
            all_frames.extend(frames)

    return all_frames


def clear_slices(slices):
    output = []
    track = []

    for frame in slices:
        key = (frame.start, frame.end)

        if key not in track:
            output.append(frame)
            track.append(key)

    return output


def test_default_test_model():
    frames = slice_2019_year()
    track = []
    for frame in frames:
        if (frame.start, frame.end) not in track:
            if frame.work_days == 10 and frame.num_events != 0 and frame.efficiency > 0.4:
                print(frame, frame.num_events)
                track.append((frame.start, frame.end))


def dump_excel():

    slices = slice_2019_year()

    n = set((frame.duration, frame.nonwork_days, frame.num_events, frame.efficiency, frame.comp_eff) for frame in slices)
    n6 = sorted(n, key=lambda e: e[4])

    df1 = pd.DataFrame([list(nn) for nn in n6],
                       index=list(range(1, len(n6) + 1)),
                       columns=['duration', 'non_work_days', 'events', 'plain_eff', 'complex_eff'])

    df1.to_excel('score_model.xlsx')


slices = clear_slices(slice_2019_year())

for frame in slices:
    # if len(set(event.city for event in frame.events)) == 1\
    #         and frame.num_events > 1\
    #         and 10 < frame.duration < 20\
    #         and frame.comp_eff == 0.45:
    print(frame, frame.comp_eff, frame.events)