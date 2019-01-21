import datetime as dt
from itertools import combinations

from vacation_tools import Planner
from data_source import events_2019, nonwork, holidays

holder = []
tracked = []

for s in range(3, 15):
    for d in range(365):
        start = dt.date(2019, 1, 1) + dt.timedelta(d)
        p = Planner(start, s, nonwork, events_2019)
        f = (p.start, p.end)

        if f not in tracked and p.duration > 2\
                and (p.duration, p.vac) not in ((3, 1), (4, 2)):
            holder.append(p)
            tracked.append(f)


HEADER = 'dur  vac  e           frame'
print(HEADER)
for frame in sorted(holder, key=lambda frame: frame.start):
    if frame.events_num > 0:
        print('{:3.0f} {:3.0f} {:3.0f}  {}'.format(frame.duration, frame.vac, frame.events_num, frame))
