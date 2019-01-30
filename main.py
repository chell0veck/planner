import datetime
import matplotlib.pyplot as plt

from vacation_tools import events_framer
from data_source import nonwork
import pickle
import time

import pandas as pd


artists = {'MONO': 201140, 'TOOL': 521019, 'PHIL': 495060,  'CBP': 78386}
events = pickle.load(open('events.p', 'rb'))


def slice_2019_year():
    all_frames = []

    for day in range(365):
        start = datetime.date(2019, 1, 1) + datetime.timedelta(day)

        for step in range(3, 20):
            frames = events_framer(start, step, nonwork, events)
            all_frames.extend(frames)

    return all_frames


def test_default_test_model():
    frames = slice_2019_year()
    track = []
    for frame in frames:
        if (frame.start, frame.end) not in track:
            if frame.work_days == 10 and frame.num_events != 0 and frame.efficiency > 0.4:
                print(frame, frame.num_events)
                track.append((frame.start, frame.end))


slices = slice_2019_year()

n = set((frame.duration, frame.nonwork_days, frame.num_events, frame.efficiency, frame.comp_eff) for frame in slices)
n6 = sorted(n, key=lambda e: e[4])


for frame in slices:
    if frame.duration == 5 and frame.nonwork_days == 3 and frame.num_events == 2:
        print(frame, frame.events)


# x = [f[0] for f in numbers]
# y = [f[1] for f in numbers]
# s = [f[2] for f in numbers]
# s_zoom = [(f[2]+1)*10 for f in numbers]
#
#
# fig, ax = plt.subplots()
# ax.scatter(x, y, s=s_zoom, c='blue')
#
# for i, txt in enumerate(s):
#     ax.annotate(str(txt), (x[i], y[i]))
#
# plt.show()
#
# for number in numbers:
#     print(number)