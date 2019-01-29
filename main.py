import datetime

from vacation_tools import events_fetcher, events_framer
from data_source import nonwork


artists = {'MONO': 201140, 'TOOL': 521019, 'PHIL': 495060,  'CBP': 78386}
events = events_fetcher(artists)


def default_test_model():
    all_frames = []

    for day in range(365):
        start = datetime.date(2019, 1, 1) + datetime.timedelta(day)

        for step in range(3, 20):
            frames = events_framer(start, step, nonwork, events)
            all_frames.extend(frames)

    return all_frames


if __name__ == '__main__':
    frames = default_test_model()

    for frame in frames:
        print(frame)
