import pandas as pd
import sys
import os
sys.path.append(os.path.abspath('..'))
from cleaning_funcs import get_percent_missing, check_for_NR, check_for_S, impute, make_plots
import numpy as np
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt


# ----------------------------------------------------------------------
# Fixing demographic data
demo = pd.read_csv('../../making_dataset/final_csv/demographics.csv')
demo = demo[~demo['LocYear'].str.contains("Alabama")]

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


# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
# Fixing economic data

econ = pd.read_csv('../../making_dataset/final_csv/econ.csv')
econ = econ[~econ['LocYear'].str.contains("Alabama")]
econ = econ[econ['LocYear'].str.len() <= 6]

econ.replace('S', 0.10, inplace=True)
econ.replace('N.A.', np.nan, inplace=True)
econ.replace('N.A.!', np.nan, inplace=True)
econ.replace('*', np.nan, inplace=True)
econ.replace('N.C.', np.nan, inplace=True)
econ.replace('<.5%', 0, inplace=True)
econ.replace('<500', 500, inplace=True)

econ['econ7'] = econ['econ7'].astype(float)
econ['econ12: 16-19'] = econ['econ12: 16-19'].astype(float)
econ['econ12: 20-24'] = econ['econ12: 20-24'].astype(float)
econ.drop('econ2', axis=1, inplace=True)

# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
# Fixing education data

educ = pd.read_csv('../../making_dataset/final_csv/educ.csv')
educ = educ[~educ['LocYear'].str.contains("Alabama")]
educ = educ[educ['LocYear'].str.len() <= 6]

educ.drop('educ1: A', axis=1, inplace=True)
educ.drop('educ1: B', axis=1, inplace=True)
educ.drop('educ1: G', axis=1, inplace=True)
educ.drop('educ1: H', axis=1, inplace=True)
educ.drop('educ1: N', axis=1, inplace=True)
educ.drop('educ2', axis=1, inplace=True)
educ.drop('educ3: IS', axis=1, inplace=True)
educ.drop('educ3: OS', axis=1, inplace=True)
educ.drop('educ5: 3', axis=1, inplace=True)
educ.drop('educ5: 1', axis=1, inplace=True)
educ.drop('educ5: 2', axis=1, inplace=True)

educ.drop('educ7: 1', axis=1, inplace=True)
educ.drop('educ7: 2', axis=1, inplace=True)
educ.drop('educ7: 3', axis=1, inplace=True)
educ.drop('educ7: 4', axis=1, inplace=True)
educ.drop('educ8: 1', axis=1, inplace=True)
educ.drop('educ8: 2', axis=1, inplace=True)
educ.drop('educ8: 3', axis=1, inplace=True)
educ.drop('educ8: 4', axis=1, inplace=True)

educ.drop('educ9: 1', axis=1, inplace=True)
educ.drop('educ9: 2', axis=1, inplace=True)
educ.drop('educ9: 3', axis=1, inplace=True)
educ.drop('educ9: 4', axis=1, inplace=True)
educ.drop('educ10: 1', axis=1, inplace=True)
educ.drop('educ10: 2', axis=1, inplace=True)
educ.drop('educ10: 3', axis=1, inplace=True)
educ.drop('educ10: 4', axis=1, inplace=True)

educ.drop('educ11: 1', axis=1, inplace=True)
educ.drop('educ11: 2', axis=1, inplace=True)
educ.drop('educ11: 3', axis=1, inplace=True)
educ.drop('educ11: 4', axis=1, inplace=True)
educ.drop('educ12: 1', axis=1, inplace=True)
educ.drop('educ12: 2', axis=1, inplace=True)
educ.drop('educ12: 3', axis=1, inplace=True)
educ.drop('educ12: 4', axis=1, inplace=True)

educ.drop('educ14: yes', axis=1, inplace=True)
educ.drop('educ14: no', axis=1, inplace=True)
educ.drop('educ15: yes', axis=1, inplace=True)
educ.drop('educ15: no', axis=1, inplace=True)
educ.drop('educ18', axis=1, inplace=True)

educ.replace('S', 0.10, inplace=True)
educ.replace('N.A.', np.nan, inplace=True)
educ.replace('N.C.', np.nan, inplace=True)
educ.replace('<.5%', 0, inplace=True)

educ['educ4'] = educ['educ4'].astype(float)
educ['educ6: H'] = educ['educ6: H'].astype(float)
educ['educ13'] = educ['educ13'].astype(float)
educ['Data'] = educ['Data'].astype(float)

# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
# Fixing family data

fam = pd.read_csv('../../making_dataset/final_csv/fam.csv')

fam = fam[~fam['LocYear'].str.contains("Alabama")]
fam = fam[fam['LocYear'].str.len() <= 6]


fam.drop('Data_x', axis=1, inplace=True)
fam.drop('Data_y', axis=1, inplace=True)
fam.drop('Data', axis=1, inplace=True)
fam.drop('fam18', axis=1, inplace=True)
fam.drop('fam19', axis=1, inplace=True)

# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
# Fixing health data

health = pd.read_csv('../../making_dataset/final_csv/health.csv')
health = health[~health['LocYear'].str.contains("Alabama")]
health = health[health['LocYear'].str.len() <= 6]

health.drop('hth12', axis=1, inplace=True)
health.drop('hth13', axis=1, inplace=True)
health.drop('hth14', axis=1, inplace=True)
health.drop('hth151617', axis=1, inplace=True)
health.drop('hth1819', axis=1, inplace=True)
health.drop('hth2021', axis=1, inplace=True)
health.drop('hth2223', axis=1, inplace=True)
health.drop('hth2425', axis=1, inplace=True)
health.drop('hth26', axis=1, inplace=True)
health.drop('hth29', axis=1, inplace=True)

health.replace('S', 0.10, inplace=True)
health.replace('N.A.', np.nan, inplace=True)
health.replace('N.C.', np.nan, inplace=True)

health['hth1_2'] = pd.to_numeric(health['hth1_2'])
health['hth3_4'] = pd.to_numeric(health['hth3_4'])
health['hth5_6'] = pd.to_numeric(health['hth5_6'])
health['hth8_9'] = pd.to_numeric(health['hth8_9'])
health['hth11'] = pd.to_numeric(health['hth11'])

# ----------------------------------------------------------------------
# Fixing safety data

safe = pd.read_csv('../../making_dataset/final_csv/safety.csv')
safe = safe[~safe['LocYear'].str.contains("Alabama")]
safe = safe[safe['LocYear'].str.len() <= 6]

safe.drop('safe1415: 1', axis=1, inplace=True)
safe.drop('safe1415: 2', axis=1, inplace=True)
safe.drop('safe161718: 1', axis=1, inplace=True)
safe.drop('safe161718: 2', axis=1, inplace=True)

safe.replace('N.R.', np.nan, inplace=True)
safe.replace('N.A.', np.nan, inplace=True)

safe.drop('safe1112: O', axis=1, inplace=True)

safe['safe7'] = pd.to_numeric(safe['safe7'])
safe['safe9_10'] = pd.to_numeric(safe['safe9_10'])
safe['safe1112: E'] = pd.to_numeric(safe['safe1112: E'])
safe['safe1112: M'] = pd.to_numeric(safe['safe1112: M'])
safe['safe1112: P'] = pd.to_numeric(safe['safe1112: P'])
safe['safe1112: S'] = pd.to_numeric(safe['safe1112: S'])
safe['Neglect'] = pd.to_numeric(safe['Neglect'])



dfs = [demo, econ, educ, fam, safe, health]

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
# make_plots(merged, imputed)

imputed['target'] = pd.qcut(imputed['hth27'], 3, labels=["Low", "Medium", "High"])
imputed.drop('hth27', axis=1, inplace=True)

# imputed.info()


scaler = StandardScaler()
good_cols = [col for col in imputed.columns if col != 'LocYear' and col != 'target']

scaled_data = scaler.fit_transform(imputed[good_cols])

scaled_df = pd.DataFrame(scaled_data, columns=good_cols, index=imputed.index)
scaled_df['LocYear'] = imputed['LocYear'] 
scaled_df['target'] = imputed['target'] 
scaled_df = scaled_df[imputed.columns]

# print(scaled_df.head())

scaled_df.to_csv('cleaned_data.csv')


'''
RangeIndex: 2116 entries, 0 to 2115
Data columns (total 83 columns):
 #   Column            Non-Null Count  Dtype   
---  ------            --------------  -----   
 0   LocYear           2116 non-null   object  
 1   d1: 0 to 4        2116 non-null   float64 
 2   d1: 12 to 14      2116 non-null   float64 
 3   d1: 15 to 17      2116 non-null   float64 
 4   d1: 5 to 11       2116 non-null   float64 
 5   d2: Female        2116 non-null   float64 
 6   d2: Male          2116 non-null   float64 
 7   d3: Foreign-born  2116 non-null   float64 
 8   d3: Native-born   2116 non-null   float64 
 9   d4: H or L        2116 non-null   float64 
 10  d4: AI or AN      2116 non-null   float64 
 11  d4: A             2116 non-null   float64 
 12  d4: B             2116 non-null   float64 
 13  d4: NH or PI      2116 non-null   float64 
 14  d4: 2 or more     2116 non-null   float64 
 15  d4: W             2116 non-null   float64 
 16  d5                2116 non-null   float64 
 17  econ1             2116 non-null   float64 
 18  econ3             2116 non-null   float64 
 19  econ4             2116 non-null   float64 
 20  econ5             2116 non-null   float64 
 21  econ6             2116 non-null   float64 
 22  econ7             2116 non-null   float64 
 23  econ8             2116 non-null   float64 
 24  econ9             2116 non-null   float64 
 25  econ10            2116 non-null   float64 
 26  econ11            2116 non-null   float64 
 27  econ12: 16-19     2116 non-null   float64 
 28  econ12: 16-24     2116 non-null   float64 
 29  econ12: 20-24     2116 non-null   float64 
 30  educ4             2116 non-null   float64 
 31  educ6: A          2116 non-null   float64 
 32  educ6: B          2116 non-null   float64 
 33  educ6: G          2116 non-null   float64 
 34  educ6: H          2116 non-null   float64 
 35  educ6: N          2116 non-null   float64 
 36  educ13            2116 non-null   float64 
 37  educ16: 3y        2116 non-null   float64 
 38  educ16: 4y        2116 non-null   float64 
 39  educ16: 5-y       2116 non-null   float64 
 40  educ16: -3y       2116 non-null   float64 
 41  educ16: tot       2116 non-null   float64 
 42  Data              2116 non-null   float64 
 43  educ19            2116 non-null   float64 
 44  fam1: A           2116 non-null   float64 
 45  fam1: B           2116 non-null   float64 
 46  fam1: G           2116 non-null   float64 
 47  fam1: H           2116 non-null   float64 
 48  fam1: N           2116 non-null   float64 
 49  fam4              2116 non-null   float64 
 50  fam5              2116 non-null   float64 
 51  fam7              2116 non-null   float64 
 52  fam8              2116 non-null   float64 
 53  fam15             2116 non-null   float64 
 54  fam16             2116 non-null   float64 
 55  safe1: 1          2116 non-null   float64 
 56  safe1: 2          2116 non-null   float64 
 57  safe4             2116 non-null   float64 
 58  safe5             2116 non-null   float64 
 59  safe6             2116 non-null   float64 
 60  safe7             2116 non-null   float64 
 61  safe9_10          2116 non-null   float64 
 62  safe1112: E       2116 non-null   float64 
 63  safe1112: M       2116 non-null   float64 
 64  Neglect           2116 non-null   float64 
 65  safe1112: P       2116 non-null   float64 
 66  safe1112: S       2116 non-null   float64 
 67  safe1920: 1       2116 non-null   float64 
 68  safe1920: 2       2116 non-null   float64 
 69  safe212223        2116 non-null   float64 
 70  hth1_2            2116 non-null   float64 
 71  hth3_4            2116 non-null   float64 
 72  hth5_6            2116 non-null   float64 
 73  hth7              2116 non-null   float64 
 74  hth8_9            2116 non-null   float64 
 75  hth10             2116 non-null   float64 
 76  hth11             2116 non-null   float64 
 77  hth28             2116 non-null   float64 
 78  hth30             2116 non-null   float64 
 79  hth31             2116 non-null   float64 
 80  hth32             2116 non-null   float64 
 81  hth33             2116 non-null   float64 
 82  target            2116 non-null   category
dtypes: category(1), float64(81), object(1)
'''
