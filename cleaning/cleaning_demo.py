import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from cleaning_funcs import get_percent_missing, check_for_NR, check_for_S, impute, make_plots

demo = pd.read_csv('../making_dataset/final_csv/demographics.csv')
demo = demo[~demo['LocYear'].str.contains("Alabama")]

# get_percent_missing(demo)

'''
Unnamed: 0: 0.0%
LocYear: 0.0%
d1: 0 to 4: 7.89%
d1: 12 to 14: 7.89%
d1: 15 to 17: 7.89%
d1: 5 to 11: 7.89%
d2: Female: 7.89%
d2: Male: 7.89%
d3: Foreign-born: 50.0%
d3: Native-born: 50.0%
d4: H or L: 35.45%
d4: AI or AN: 35.45%
d4: A: 35.45%
d4: B: 35.45%
d4: NH or PI: 35.45%
d4: 2 or more: 35.45%
d4: W: 35.45%
d5: 44.74%
'''

'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 2014 entries, 0 to 2013
Data columns (total 18 columns):
 #   Column            Non-Null Count  Dtype  
---  ------            --------------  -----  
 0   Unnamed: 0        2014 non-null   int64  
 1   LocYear           2014 non-null   object 
 2   d1: 0 to 4        1855 non-null   object 
 3   d1: 12 to 14      1855 non-null   object 
 4   d1: 15 to 17      1855 non-null   object 
 5   d1: 5 to 11       1855 non-null   object 
 6   d2: Female        1855 non-null   object 
 7   d2: Male          1855 non-null   object 
 8   d3: Foreign-born  1007 non-null   object 
 9   d3: Native-born   1007 non-null   object 
 10  d4: H or L        1300 non-null   float64
 11  d4: AI or AN      1300 non-null   float64
 12  d4: A             1300 non-null   float64
 13  d4: B             1300 non-null   float64
 14  d4: NH or PI      1300 non-null   float64
 15  d4: 2 or more     1300 non-null   float64
 16  d4: W             1300 non-null   float64
 17  d5                1113 non-null   object 
dtypes: float64(7), int64(1), object(10)
memory usage: 283.3+ KB
'''

demo.replace('S', 0.10, inplace=True)
demo.replace('N.A.', np.nan, inplace=True)
demo.replace('N.A.!', np.nan, inplace=True)
demo.replace('*', np.nan, inplace=True)
demo.replace('N.C.', np.nan, inplace=True)
demo.replace('<.5%', 0, inplace=True)
demo.replace('<500', 500, inplace=True)

demo['d1: 0 to 4'] = demo['d1: 0 to 4'].astype(float)
demo['d1: 12 to 14'] = demo['d1: 12 to 14'].astype(float)
demo['d1: 15 to 17'] = demo['d1: 15 to 17'].astype(float)
demo['d1: 5 to 11'] = demo['d1: 5 to 11'].astype(float)

demo['d2: Female'] = demo['d2: Female'].astype(float)
demo['d2: Male'] = demo['d2: Male'].astype(float)
demo['d3: Foreign-born'] = demo['d3: Foreign-born'].astype(float)
demo['d3: Native-born'] = demo['d3: Native-born'].astype(float)
demo['d5'] = demo['d5'].astype(float)

# demo.info()

imputed = demo.copy()
imputed = impute(demo, imputed)
# make_plots(demo, imputed)

'''
d3 -> shady, not bad
d4 -> shady, not bad
d5 same thing
'''