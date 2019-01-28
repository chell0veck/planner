
from vacation_tools import Framer, fetch_events
from data_source import nonwork
import datetime


artist = {'MONO': 201140, 'TOOL': 521019, 'PHIL': 495060,  'CBP': 78386}
events = fetch_events(artist)


def default_test_model():
    output = []

    for day in range(365):
        start = datetime.date(2019, 1, 1) + datetime.timedelta(day)

        for step in range(3, 20):
            p = Framer(start, step, nonwork, events)
            if p.efficiency > 0.5 and p.events_num == 2:
                output.append(p)

    return output


l = default_test_model()


for p in l:
    print('{} - {:2} - {:2} - {:2} - {:4} - {}'.format(p, p.vac, p.duration, p.events_num, p.efficiency, p.view_events()))