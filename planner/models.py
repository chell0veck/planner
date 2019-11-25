#!/usr/bin/env python3

import datetime
from itertools import groupby
from collections import defaultdict
import json
from config import SEPARATOR, SKIP_COUNTRIES
import utils as ut


def view_by_group(events, group, skip=True):
    contain = defaultdict(list)

    if skip:
        skip_ctrys = json.load(open(SKIP_COUNTRIES))
        events = [event for event in events if event['country'] not in skip_ctrys]

    for event in events:
        contain[event[group]].append(event)

    for group, values in contain.items():
        print('\n---{}---'.format(group))
        for v in sorted(values, key=lambda e: e['date']):
            print(v['artist'], v['date'], v['city'])
        print('total: {}'.format(len(values)))