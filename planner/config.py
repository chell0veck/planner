"""
This file defines all static data:

Namely:
    songkick api key;
    cache data
    cache time
    countries to skip
    artists to track
    ? and something about holidays, not yet defined
"""

import os
from pathlib import Path

STATIC_FOLDER = os.path.join(Path(__file__).parents[0], 'static')
CACHE_DATA_FILE = 'cache.json'
CACHE_TIME_FILE = 'cache.utc_time'
STATIC_ARTISTS_FILE = 'artists.json'
STATIC_SKIP_COUNTRIES = 'skip_countries.json'

SEPARATOR = '\n ------ {} ------'

SGK_API_URL = 'https://api.songkick.com/api/3.0/artists/{}/calendar.json?apikey={}'
SGK_API_KEY = open(os.path.join(STATIC_FOLDER, '.songkick_api_key'), 'r').read()
CACHE_DATA = os.path.join(STATIC_FOLDER, CACHE_DATA_FILE)
CACHE_TIME = os.path.join(STATIC_FOLDER, CACHE_TIME_FILE)
SKIP_COUNTRIES = os.path.join(STATIC_FOLDER, STATIC_SKIP_COUNTRIES)
ARTISTS = os.path.join(STATIC_FOLDER, STATIC_ARTISTS_FILE)
