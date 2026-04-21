import pandas as pd
import sys
import os
sys.path.append(os.path.abspath('..'))
from cleaning_funcs import get_percent_missing, check_for_NR, check_for_S, impute, make_plots

demo = pd.read_csv('clean_demo.csv')
econ = pd.read_csv('clean_econ.csv')
educ = pd.read_csv('clean_educ.csv')
fam = pd.read_csv('clean_fam.csv')
safety = pd.read_csv('clean_safety.csv')
health = pd.read_csv('clean_health.csv')

dfs = [demo, econ, educ, fam, safety, health]

for df in dfs:
    df.drop('Unnamed: 0', axis=1, inplace=True)

# Aggregate duplicate LocYear rows before merging
dfs = [df.groupby('LocYear', as_index=False).first() for df in dfs]

merged = dfs[0]
for df in dfs[1:]:
    merged = pd.merge(merged, df, on='LocYear', how='outer')

merged = merged[~merged['LocYear'].str.contains("Alabama")]
# merged.to_csv('cleaned_data.csv', index=False)

# merged.info()

imputed = merged.copy()
imputed = impute(merged, imputed)
make_plots(merged, imputed)

imputed.to_csv('cleaned_data.csv', index=False)

'''
<class 'pandas.core.frame.DataFrame'>
Index: 2116 entries, 0 to 2164
Data columns (total 83 columns):
 #   Column            Non-Null Count  Dtype  
---  ------            --------------  -----  
 0   LocYear           2116 non-null   object 
 1   d1: 0 to 4        2014 non-null   float64
 2   d1: 12 to 14      2014 non-null   float64
 3   d1: 15 to 17      2014 non-null   float64
 4   d1: 5 to 11       2014 non-null   float64
 5   d2: Female        2014 non-null   float64
 6   d2: Male          2014 non-null   float64
 7   d3: Foreign-born  2014 non-null   float64
 8   d3: Native-born   2014 non-null   float64
 9   d4: H or L        2014 non-null   float64
 10  d4: AI or AN      2014 non-null   float64
 11  d4: A             2014 non-null   float64
 12  d4: B             2014 non-null   float64
 13  d4: NH or PI      2014 non-null   float64
 14  d4: 2 or more     2014 non-null   float64
 15  d4: W             2014 non-null   float64
 16  d5                2014 non-null   float64
 17  econ1             1307 non-null   float64
 18  econ3             1307 non-null   float64
 19  econ4             1307 non-null   float64
 20  econ5             1307 non-null   float64
 21  econ6             1307 non-null   float64
 22  econ7             1307 non-null   float64
 23  econ8             1307 non-null   float64
 24  econ9             1307 non-null   float64
 25  econ10            1307 non-null   float64
 26  econ11            1307 non-null   float64
 27  econ12: 16-19     1307 non-null   float64
 28  econ12: 16-24     1307 non-null   float64
 29  econ12: 20-24     1307 non-null   float64
 30  educ4             1918 non-null   float64
 31  educ6: A          1918 non-null   float64
 32  educ6: B          1918 non-null   float64
 33  educ6: G          1918 non-null   float64
 34  educ6: H          1918 non-null   float64
 35  educ6: N          1918 non-null   float64
 36  educ13            1918 non-null   float64
 37  educ16: 3y        1918 non-null   float64
 38  educ16: 4y        1918 non-null   float64
 39  educ16: 5-y       1918 non-null   float64
 40  educ16: -3y       1918 non-null   float64
 41  educ16: tot       1918 non-null   float64
 42  Data              1918 non-null   float64
 43  educ19            1918 non-null   float64
 44  fam1: A           1785 non-null   float64
 45  fam1: B           1785 non-null   float64
 46  fam1: G           1785 non-null   float64
 47  fam1: H           1785 non-null   float64
 48  fam1: N           1785 non-null   float64
 49  fam4              1785 non-null   float64
 50  fam5              1785 non-null   float64
 51  fam7              1785 non-null   float64
 52  fam8              1785 non-null   float64
 53  fam15             1785 non-null   float64
 54  fam16             1785 non-null   float64
 55  safe1: 1          1275 non-null   float64
 56  safe1: 2          1275 non-null   float64
 57  safe4             1275 non-null   float64
 58  safe5             1275 non-null   float64
 59  safe6             1275 non-null   float64
 60  safe7             1275 non-null   float64
 61  safe9_10          1275 non-null   float64
 62  safe1112: E       1275 non-null   float64
 63  safe1112: M       1275 non-null   float64
 64  Neglect           1275 non-null   float64
 65  safe1112: P       1275 non-null   float64
 66  safe1112: S       1275 non-null   float64
 67  safe1920: 1       1275 non-null   float64
 68  safe1920: 2       1275 non-null   float64
 69  safe212223        1275 non-null   float64
 70  hth1_2            1785 non-null   float64
 71  hth3_4            1785 non-null   float64
 72  hth5_6            1785 non-null   float64
 73  hth7              1785 non-null   float64
 74  hth8_9            1785 non-null   float64
 75  hth10             1785 non-null   float64
 76  hth11             1785 non-null   float64
 77  hth28             1785 non-null   float64
 78  hth30             1785 non-null   float64
 79  hth31             1785 non-null   float64
 80  hth32             1785 non-null   float64
 81  hth33             1785 non-null   float64
 82  target            1785 non-null   object 
dtypes: float64(81), object(2)
memory usage: 1.4+ MB
'''

