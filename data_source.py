import datetime as dt

HOLS = [(2019, 1, 1), (2019, 1, 7), (2019, 3, 8), (2019, 4, 29),
        (2019, 5, 1), (2019, 5, 9), (2019, 6, 17), (2019, 6, 28),
        (2019, 8, 26), (2019, 10, 14), (2019, 12, 25), (2019, 12, 31), (2020, 1, 1), (2020, 1, 7)]


holidays = [dt.date(*i) for i in HOLS]


weekends = [(dt.date(2019, 1, 1) + dt.timedelta(i)) for i in range(365)
            if (dt.date(2019, 1, 1) + dt.timedelta(i)).weekday() in (5, 6)]

nonwork = holidays + weekends


