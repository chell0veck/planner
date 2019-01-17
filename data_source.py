import datetime as dt

HOLS = [(2019, 1, 1), (2019, 1, 7), (2019, 3, 8), (2019, 4, 29),
        (2019, 5, 1), (2019, 5, 9), (2019, 6, 17), (2019, 6, 28),
        (2019, 8, 26), (2019, 10, 14), (2019, 12, 25), (2019, 12, 31), (2020, 1, 1), (2020, 1, 7)]

TOOL = [((2019, 5, 5), 'Jacksonville, FL', '...'), ((2019, 6, 2), 'Berlin, DE', 'Benz Arena'),
        ((2019, 6, 4), 'Prague, CZ', 'O2'), ((2019, 6, 5), 'Vienna, AT', 'Stadthalle'),
        ((2019, 6, 7), 'Nuremberg, DE', 'Rock am Ring'), ((2019, 6, 9), 'Nuremberg, DE', 'Rock am Ring'),
        ((2019, 6, 11), 'Krakow, PL', 'Impact festival'), ((2019, 6, 13), 'Florence, IT', 'Ipodromo'),
        ((2019, 6, 16), 'Donington, UK', 'Park'), ((2019, 6, 18), 'Amsterdam, NL', 'Ziggo Dome'),
        ((2019, 6, 20), 'Copenhagen, DK', 'Fest'), ((2019, 6, 23), 'Clisson, FR', '...'),
        ((2019, 6, 25), 'Zurich, CH', 'Hallenstadion'), ((2019, 6, 28), 'Werchter, BE', 'Festivalpark'),
        ((2019, 6, 30), 'Madrid, ES', 'Downlaod Mardid'), ((2019, 7, 2), 'Lisbon, PT', '...`')]


CBP = [((2019, 3, 21), 'London, UK', ' Underworl'), ((2019, 3, 24), 'Hamburg, DE', ' Knus'),
       ((2019, 3, 25), 'Aarhus, DK', ' Voxhal'), ((2019, 3, 26), 'Stockholm, SE', ' Krake'),
       ((2019, 3, 27), 'Copenhagen, DK', ' Veg'), ((2019, 3, 28), 'Berlin, DE', ' BiNu'),
       ((2019, 3, 29), 'Dresden, DE', ' Scheun'), ((2019, 3, 30), 'Prague, CZ', ' Underdog'),
       ((2019, 4, 1), 'Aschaffenburg, DE', ' Colossaa'), ((2019, 4, 2), 'Martigny, CH', ' Caves du Manoi'),
       ((2019, 4, 3), 'Vaureal, FR', ' Le Foru'), ((2019, 4, 4), 'Strasbourg, FR', ' La Laiteri'),
       ((2019, 4, 5), 'Nimes, FR', ' La Palom'), ((2019, 4, 6), 'Luzern, CH', ' Schüü'),
       ((2019, 4, 7), 'Villingen Schwenningen, DE', ' Kolsterho'), ((2019, 4, 8), 'Vienna, AT', ' Aren'),
       ((2019, 4, 9), 'Munich, DE', ' Feierwer'), ((2019, 4, 10), 'Cologne, DE', ' Luxo'),
       ((2019, 4, 11), 'Tilburg, NL', ' Roadburn Festival (CBP & Fotocrime)'),
       ((2019, 4, 12), 'Tilburg, NL', ' Roadburn Festival (Soft Kil)')]

PHC = [((2019, 6, 2), 'Vienna, AT', 'Ernst Happel Stadion'), ((2019, 6, 4), 'Lyon, FR', 'Grouplama Stadium'),
       ((2019, 6, 5), 'Stuttgart, DE', 'Mercedes-Benz Arena'), ((2019, 6, 7), 'Berlin, DE', 'Olympiastadion'),
       ((2019, 6, 8), 'Aarhus, DK', 'Ceres Park'), ((2019, 6, 10), 'Bergen, NO', 'Bergenhus ...'),
       ((2019, 6, 12), 'Stockholm, SE', 'Friends Arena*'), ((2019, 6, 14), 'Hannover, DE', 'HDI Arena'),
       ((2019, 6, 15), 'Hannover, DE', 'HDI Arena'), ((2019, 6, 17), 'Milan, IT', 'Mediolanum Forum'),
       ((2019, 6, 18), 'Zurich, CH', 'Stadion Letzigrund'), ((2019, 6, 20), 'Nijmegen, NL', 'Goffertpark'),
       ((2019, 6, 21), 'Cologne, DE', 'Rheinenergiestation'), ((2019, 6, 22), 'Cologne, DE', 'Rheinenergiestation'),
       ((2019, 6, 24), 'Munich, DE', 'Olympiastadion'), ((2019, 6, 25), 'Prague, CZ', 'O2 Arena'),
       ((2019, 6, 26), 'Warsaw, PL', 'PGE Narodowy')]

holidays = [dt.date(*i) for i in HOLS]
TOOL = [('TOOL', dt.date(*i[0]), i[1], i[2]) for i in TOOL]
CBP = [('CBP', dt.date(*i[0]), i[1], i[2]) for i in CBP]
PHC = [('PHIL', dt.date(*i[0]), i[1], i[2]) for i in PHC]

events_2019 = TOOL + CBP + PHC
weekends = [(dt.date(2019, 1, 1) + dt.timedelta(i)) for i in range(365)
               if (dt.date(2019, 1, 1) + dt.timedelta(i)).weekday() in (5, 6)]

nonwork = holidays + weekends


