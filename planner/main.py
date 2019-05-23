import songkick as sk
import models as md
import utils

events = sk.load_events()
md.view_by_artist(events)

