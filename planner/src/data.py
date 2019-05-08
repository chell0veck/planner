""" """


import datetime


RAW_HOLS = [(2019, 1, 1), (2019, 1, 7), (2019, 3, 8), (2019, 4, 29), (2019, 5, 1),
            (2019, 5, 9), (2019, 6, 17), (2019, 6, 28), (2019, 8, 26), (2019, 10, 14),
            (2019, 12, 25), (2019, 12, 31), (2020, 1, 1), (2020, 1, 7)]

FMT_HOLS = [datetime.date(*i) for i in RAW_HOLS]

WEEKENDS = [(datetime.date(2019, 1, 1) + datetime.timedelta(i)) for i in range(365)
            if (datetime.date(2019, 1, 1) + datetime.timedelta(i)).weekday() in (5, 6)]

NON_WORK = FMT_HOLS + WEEKENDS

SKIP_CTRY = ('Japan', 'New Zealand', 'Australia', 'US', 'Canada', 'China')

ARTISTS = {'Mono': 201140, 'Tool': 521019, 'CBP': 78386, 'APC': 549892, 'Puscifer': 594931,
           'Damien Rice': 391954, 'Caspian': 508722, 'Bell X1': 78581, 'EXP': 561284, 'Mogwai': 70202,
           'Sigur Rós': 496602, 'The National': 405285, 'Chevelle': 480448, 'Editors': 306990,
           'Yndi Halda': 4768, 'The Seven Mile Journey': 368079}

# todo: it should be stored somehow better