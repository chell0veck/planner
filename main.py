"""
Entry point of a program. So far just change the view model from md lib
"""

import songkick as sk
import models as md


events = sk.load_events()
md.view_by_month(events)
