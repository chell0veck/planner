"""
Entry point of a program. So far just change the view model from md lib
"""

import songkick
import date_utils
from data_utils import Day

events = songkick.load_events()
frames = date_utils.generate_frames()
frame = list(frames)[12]


def wrap_events_into_frame(frame, events):
    frame_start, frame_end = frame
    result = []

    for event in events:
        if frame_start <= event.date <= frame_end:
            result.append(Day(event.date, event, date_utils.is_non_working(event.date)))

    return result
