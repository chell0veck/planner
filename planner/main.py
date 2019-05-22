import songkick as sk
import models as md
import utils

# sk.refresh_cache()
# events = sk.load_cache()
#
#
# md.view_by_month(events)

# artists = utils.load_artists('_static_artists.json')
# sk.dump_cache(artists)
events = sk.load_events()
md.view_by_month(events)