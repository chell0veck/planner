import songkick as sk
import models as md

events = sk.load_events()
md.view_by_month(events)