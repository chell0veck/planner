from utils import load_artist_from_file
from config import ARTISTS, SKIP_COUNTRIES
import songkick as sk
from datatypes import Event, EventProcessor
from models import view_by_group

artists = load_artist_from_file(ARTISTS)
events = [Event(**event) for event in sk.load_events()]
#
e = EventProcessor(events).process()
# print(e)
# events = sk.load_events()
# view_by_group(events, 'artist', skip=True)
