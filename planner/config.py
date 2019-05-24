import os
from pathlib import Path

static_folder = os.path.join(Path(__file__).parents[0],'static')
cache_data_file = 'cache.json'
cache_time_file = 'cache.utc_time'
static_artist = 'artists.json'
static_skip_countries = 'skip_countries.json'

separator = '\n ------ {} ------'

sgk_api_url = 'https://api.songkick.com/api/3.0/artists/{}/calendar.json?apikey={}'
sgk_api_key = open(os.path.join(static_folder, '.songkick_api_key'), 'r').read()
cache_data = os.path.join(static_folder, cache_data_file)
cache_time = os.path.join(static_folder, cache_time_file)
skip_countries = os.path.join(static_folder, static_skip_countries)
artists = os.path.join(static_folder, static_artist)
