# Planner

Vacation planner intends to help optimise vacation planning.

- with less number of vacations visit most of events.
- spend vacation most efficiently that not determined yet. 

As of now consists of 2 data structures (Event, Frame) and to wrapers (events_fetcher and 
events_framer)

events_fetcher wraps 'events' into Event object where 'events' - api response from
songckiker based on interested artists

Event knows date, performes, venue, city, country information.

events_framer slices given period of time into Frame objects. It also adjusts
period start, end if it's not working days.

Frame object holds unique set of events and some other info and  will be used to calculate
its efficiency.

And the test model (default_test_model) prints all frames for 2019 with plaint efficiency within 20 days of 
period

