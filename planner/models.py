import datetime

from collections import defaultdict


def view_by_artist(events):
    container = defaultdict(list)
    template = '\n ------ {} ------'

    for event in events:
        container[event.artist].append(event)

    for artist in container:
        print(template.format(artist))

        for event in container[artist]:
            print(event)


def view_by_month(events):
    container = defaultdict(list)
    template = '\n ------ {} ------'

    for event in events:
        month = datetime.date.strftime(event.date, '%B')
        container[month].append(event)

    for month in container:
        print(template.format(month))

        for event in container[month]:
            print(event)


def view_by_country(events):
    container = defaultdict(list)
    template = '\n ------ {} ------'
    events = [container[event.country].append(event) for event in events]

    for header in events:
        print(template.format(header))

        for event in container[header]:
            print(event)