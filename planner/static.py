import json
import os
from pathlib import Path

import calendarific
# import songkick

skip_ctry = json.load(open('_static_skip_ctry.json', 'r'))
artists = json.load(open('_static_artists.json', 'r'))

