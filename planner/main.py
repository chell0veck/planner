import songkick as sk
import models as md


# sk.refresh_cache()
events = sk.load_cache()


md.view_by_month(events)
