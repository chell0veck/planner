import os


static_folder = 'static'
static_cache_file = 'cache.json'
static_cache_time = 'cache.time'
static_artist = 'artists.json'
static_skip_countries = 'skip_countries.json'


separator = '\n ------ {} ------'

sgk_api_url = 'https://api.songkick.com/api/3.0/artists/{}/calendar.json?apikey={}'
sgk_api_key = open(os.path.join(static_folder, '.songkick_api_key'), 'r').read()
cache_data = os.path.join(os.getcwd(), static_folder, static_cache_file)
cache_time = os.path.join(os.getcwd(), static_folder, static_cache_time)
skip_countries = os.path.join(static_folder, static_skip_countries)
artists = os.path.join(os.getcwd(), static_folder, static_artist)
