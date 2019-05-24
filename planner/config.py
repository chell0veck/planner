sgk_api_url = 'https://api.songkick.com/api/3.0/artists/{}/calendar.json?apikey={}'
sgk_api_key = open('.songkick_api_key', 'r').read()
skip_ctrys = '_static_skip_ctry.json'
cache_data = '_static_events.json'
cache_time = '_static_events.time'
artists = '_static_artists.json'
separator = '\n ------ {} ------'
