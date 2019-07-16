"""
Defines actual modules to view events of interest.
It's actually most important here - logic.

Functions:
    view_by_artist
    view_by_month
    view_by_county

"""

import datetime

from collections import defaultdict

from config import SEPARATOR


def view_by_artist(events, sep=SEPARATOR):
    """
    Print sorted list of Event object sorted by artist
    :param events: list of Event objects
    :param sep: str (default header)
    :return: None
    """
    container = defaultdict(list)

    for event in events:
        container[event.artist].append(event)

    for artist in container:
        print(sep.format(artist))

        for event in container[artist]:
            print(event.date)


def view_by_month(events, sep=SEPARATOR):
    """
    Print sorted list of Event object sorted by month
    :param events: list of Event objects
    :param sep: str (default header)
    :return: None
    """
    container = defaultdict(list)

    for event in events:
        month = datetime.date.strftime(event.date, '%B')
        container[month].append(event)

    for month in container:
        print(sep.format(month))

        for event in container[month]:
            print(event)


def view_by_country(events, sep=SEPARATOR):
    """
    Print sorted list of Event object sorted by country
    :param events: list of Event objects
    :param sep: str (default header)
    :return: None
    """
    container = defaultdict(list)

    for event in events:
        container[event.country].append(event)

    for country in container:
        print(sep.format(country))

        for event in container[country]:
            print(event)


