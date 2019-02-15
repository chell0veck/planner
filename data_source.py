import datetime

HOLS = [(2019, 1, 1), (2019, 1, 7), (2019, 3, 8), (2019, 4, 29), (2019, 5, 1), (2019, 5, 9), (2019, 6, 17),
        (2019, 6, 28), (2019, 8, 26), (2019, 10, 14), (2019, 12, 25), (2019, 12, 31), (2020, 1, 1), (2020, 1, 7)]

holidays = [datetime.date(*i) for i in HOLS]

weekends = [(datetime.date(2019, 1, 1) + datetime.timedelta(i)) for i in range(365)
            if (datetime.date(2019, 1, 1) + datetime.timedelta(i)).weekday() in (5, 6)]

nonwork = holidays + weekends

skip = ('Japan', 'New Zealand', 'Australia', 'UK', 'US', 'Canada', 'China')

artists = {'MONO': 201140, 'TOOL': 521019, 'PHIL': 495060,  'CBP': 78386, 'APC': 549892, 'Puscifer': 594931,
           'Damien Rice': 391954, 'Caspian': 508722, 'Bell X1': 78581, 'EXP': 561284, 'Mogwai': 70202,
           'Sigur Rós': 496602}
