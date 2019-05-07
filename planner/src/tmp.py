import datetime
import itertools
import requests
import os
from pathlib import Path
from .tools import Event, Frame


def events_framer(start, step, holidays, events=None):
    all_frames = []
    end = start + datetime.timedelta(step - 1)

    while end + datetime.timedelta(1) in holidays:
        end += datetime.timedelta(1)

    while start - datetime.timedelta(1) in holidays:
        start -= datetime.timedelta(1)

    nonworking_days = set(day for day in holidays if start <= day <= end)

    if events:
        events_matches = [event for event in events if start < event.date < end]
        artists_number = len(set(event.artist for event in events_matches))
        events_combo = [itertools.combinations(events_matches, i) for i in range(1, artists_number+1)]

        for events_set in events_combo:
            for events in events_set:

                if len(events) == 1:
                    all_frames.append(Frame(start, end, events, nonworking_days))

                else:
                    all_evts = len(events)
                    uniq_art = len(set(event.artist for event in events))
                    uniq_dts = len(set(event.date for event in events))

                    if uniq_art == all_evts and uniq_dts == all_evts:
                        all_frames.append(Frame(start, end, events, nonworking_days))

    all_frames.append(Frame(start, end, [], nonworking_days))

    return all_frames


def slice_this_year(nonwork, events):
    all_frames = []

    for day in range(365):
        start = datetime.date(2019, 1, 1) + datetime.timedelta(day)

        for step in range(3, 20):
            frames = events_framer(start, step, nonwork, events)

            all_frames.extend(frames)

    return all_frames