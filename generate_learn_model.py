import random

import pandas as pd


vacation = [random.randint(0, 20) for _ in range(100)]

duration = []
for i in vacation:
    dur = random.randint(i, 20)
    duration.append(dur)



# duration = [random.randint(0, 21) for _ in range(100)]
events = [random.randint(0, 5) for _ in range(100)]
places = [random.randint(1, 5) for _ in range(100)]


vac = pd.DataFrame({'vacation': vacation}, index=[i for i in range(len(vacation))])
dur = pd.DataFrame({'duration': duration}, index=[i for i in range(len(duration))])
eve = pd.DataFrame({'events': events}, index=[i for i in range(len(events))])
pla = pd.DataFrame({'places': places}, index=[i for i in range(len(places))])

frames = [vac, dur, eve, pla]
out = pd.concat(frames, axis=1, sort=True)


writer = pd.ExcelWriter('learn_dataset.xlsx')
out.to_excel(writer, 'Sheet3')
writer.save()
