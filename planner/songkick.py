from datetime import datetime
import json
import requests
from utils import load_artist_from_file
from config import SGK_API_URL, SGK_API_KEY, CACHE_DATA, CACHE_TIME


def _cache_is_stale():
    with open(CACHE_TIME, 'r') as cache_time:
        cache_utc_time = datetime.strptime(cache_time.read(), '%Y-%m-%d %H:%M:%S.%f')
    curr_utc_time = datetime.utcnow()
    diff = curr_utc_time - cache_utc_time
    if diff.days >= 1:
        return True
    return False


def _build_api_url(artist_id):
    url = SGK_API_URL.format(artist_id, SGK_API_KEY)
    return url


def _validate_response(response):
    response_ok = response['resultsPage']['status'] == 'ok'
    events_exist = 'event' in response['resultsPage']['results']
    return response_ok and events_exist


def get_events_by_artist(artist_name, artist_id):
    url = _build_api_url(artist_id)
    res = requests.get(url).json()
    valid_response = _validate_response(res)
    events_list = []

    if valid_response:
        events = res['resultsPage']['results']['event']

        for event in events:
            event_artists = [e['displayName'] for e in event['performance']]
            event_display = event['displayName']
            event_date = event['start']['date']
            event_type = event['type']
            event_uri = event['uri']
            event_venue = event['venue']['displayName']
            event_country = event['venue']['metroArea']['country']['displayName']
            event_city = event['venue']['metroArea']['displayName']
            events_list.append({'artist': artist_name, 'artists': event_artists,
                                'display': event_display, 'date': event_date,
                                'type': event_type, 'uri': event_uri, 'venue': event_venue,
                                'country': event_country, 'city': event_city})
    return events_list


def get_events_by_artists(artists_map):
    events = []
    for artist_name, artist_id in artists_map.items():
        artist_events = get_events_by_artist(artist_name, artist_id)
        if artist_events:
            events.extend(artist_events)
    return events


def dump_cache(cache_data):
    timestamp = datetime.now()

    with open(CACHE_DATA, 'w') as c_d:
        json.dump(cache_data, c_d)

    with open(CACHE_TIME, 'w') as c_t:
        c_t.write(str(timestamp.utcnow()))


def load_cache():
    with open(CACHE_DATA) as cache_data:
        return json.load(cache_data)


def refresh_cache():
    artists = load_artist_from_file()
    events = get_events_by_artists(artists)
    dump_cache(events)


def load_events():
    cache_is_stale = _cache_is_stale()
    if cache_is_stale:
        refresh_cache()
    events = load_cache()
    return events
