import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from cleaning_funcs import get_percent_missing, check_for_NR, check_for_S, impute, make_plots
from sklearn.preprocessing import StandardScaler

econ = pd.read_csv('../making_dataset/final_csv/econ.csv')
econ = econ[~econ['LocYear'].str.contains("Alabama")]
econ = econ[econ['LocYear'].str.len() <= 6]

get_percent_missing(econ)

'''
Unnamed: 0: 0.0%
LocYear: 0.0%
econ1: 6.11%
econ2: 43.67%
econ3: 6.11%
econ4: 9.87%
econ5: 32.4%
econ6: 28.65%
econ7: 3.76%
econ8: 28.65%
econ9: 39.91%
econ10: 24.89%
econ11: 28.65%
econ12: 16-19: 39.91%
econ12: 16-24: 39.91%
econ12: 20-24: 39.91%
'''

econ.info()
'''
<class 'pandas.DataFrame'>
Index: 1358 entries, 0 to 2228
Data columns (total 16 columns):
 #   Column         Non-Null Count  Dtype  
---  ------         --------------  -----  
 0   Unnamed: 0     1358 non-null   int64  
 1   LocYear        1358 non-null   str    
 2   econ1          1275 non-null   float64
 3   econ2          765 non-null    float64
 4   econ3          1275 non-null   float64
 5   econ4          1224 non-null   float64
 6   econ5          918 non-null    float64
 7   econ6          969 non-null    float64
 8   econ7          1307 non-null   str    
 9   econ8          969 non-null    float64
 10  econ9          816 non-null    float64
 11  econ10         1020 non-null   float64
 12  econ11         969 non-null    float64
 13  econ12: 16-19  816 non-null    str    
 14  econ12: 16-24  816 non-null    float64
 15  econ12: 20-24  816 non-null    str    
dtypes: float64(11), int64(1), str(4)
memory usage: 200.2 KB
'''

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

imputed = econ.copy()
imputed = impute(econ, imputed)
# make_plots(econ, imputed)

imputed.drop('econ2', axis=1, inplace=True)

scaler = StandardScaler()
good_cols = [col for col in imputed.columns if col != 'LocYear']

scaled_data = scaler.fit_transform(imputed[good_cols])

scaled_df = pd.DataFrame(scaled_data, columns=good_cols, index=imputed.index)
scaled_df['LocYear'] = imputed['LocYear'] 

scaled_df = scaled_df[imputed.columns]

scaled_df.drop('Unnamed: 0', axis=1, inplace=True)

print(scaled_df.head())

make_plots(scaled_df, scaled_df)

'''
possibly bad list
econ2
econ5
econ6
econ8
econ9
econ10
econ11
econ12
'''