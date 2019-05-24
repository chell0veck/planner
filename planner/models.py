import datetime

from collections import defaultdict

from config import separator


def view_by_artist(events, sep=separator):
    container = defaultdict(list)

    for event in events:
        container[event.artist].append(event)

    for artist in container:
        print(sep.format(artist))

        for event in container[artist]:
                print(event)


def view_by_month(events, sep=separator):
    container = defaultdict(list)

    for event in events:
        month = datetime.date.strftime(event.date, '%B')
        container[month].append(event)

    for month in container:
        print(sep.format(month))

        for event in container[month]:
            print(event)


def view_by_country(events, sep=separator):
    container = defaultdict(list)

    for event in events:
        container[event.country].append(event)

    for country in container:
        print(sep.format(country))

        for event in container[country]:
            print(event)
