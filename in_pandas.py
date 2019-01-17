import warnings
warnings.filterwarnings("ignore", message="numpy.dtype size changed")
import pandas as pd

from data_source import HOLS, TOOL, CBP, PHC


pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 500)


hol = pd.DataFrame({'HOL': ['HOL' for _ in range(len(HOLS))]}, index=[d for d in HOLS])
tool = pd.DataFrame({'tool': [d[0] for d in TOOL]}, index=[d[1] for d in TOOL])
cbp = pd.DataFrame({'cbp': [d[0] for d in CBP]}, index=[d[1] for d in CBP])
phil = pd.DataFrame({'Phill': [d[0] for d in PHC]}, index=[d[1] for d in PHC])

frames = [hol, tool, cbp, phil]
out = pd.concat(frames, axis=1, sort=True, join='outer').fillna('.')
out['day'] = pd.to_datetime(out.index).strftime('%A')
out['w_num'] = pd.to_datetime(out.index).strftime('%W')
print(out)
