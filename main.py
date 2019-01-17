import datetime as dt

from vacation_tools import Planner
from data_source import events_2019, nonwork, holidays


# start = dt.date(2019, 6, 18)
# step = 10
#
# for take_into_account in [None, holidays, nonwork]:
#     f = Planner(start, step, take_into_account, events_2019)
#     print('{:.2f} : {:3.0f} : {:3.0f} : {}'.format(f.efficiency, f.duration, f.match_events(), f))


holder = []
tracked = []

for step in range(2, 20):
    for d in range(365):
        start = dt.date(2019, 1, 1) + dt.timedelta(d)
        p = Planner(start, step, nonwork, events_2019)
        f = (p.start, p.end)

        if f not in tracked and p.duration > 2\
                and (p.duration, p.vac) not in ((3, 1), (4, 2)):
            holder.append(p)
            tracked.append(f)

for frame in sorted(holder, key=lambda frame: frame.efficiency, reverse=True)[:100]:
    print('{:3.2f} {:3.0f} {:3.0f}  {}'.format(frame.efficiency,
                                               frame.duration, frame.vac, frame))

