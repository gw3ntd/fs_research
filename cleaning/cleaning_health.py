import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from cleaning_funcs import get_percent_missing, check_for_NR, check_for_S, impute, make_plots, plot_one
from sklearn.preprocessing import StandardScaler

health = pd.read_csv('../making_dataset/final_csv/health.csv')

'''
Unnamed: 0: 0.0%
LocYear: 0.0%
hth1_2: 15.02%
hth3_4: 16.09%
hth5_6: 16.09%
hth7: 2.11%
hth8_9: 16.09%
hth10: 33.31%
hth11: 2.11%
hth12: 58.09% # drop
hth13: 91.39% # this is actually crazt
hth14: 73.11% # drop
hth151617: 81.71% # drop
hth1819: 81.71% # drop
hth2021: 73.11% # drop
hth2223: 73.11% # drop
hth2425: 72.03% # drop
hth26: 83.86% # drop
hth27: 2.11%
hth28: 2.11%
hth29: 72.03% # drop
hth30: 2.11%
hth31: 2.11%
hth32: 2.11%
hth33: 2.11%
'''

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

# get_percent_missing(health)

'''
Unnamed: 0: 0.0%
LocYear: 0.0%
hth1_2: 15.02%
hth3_4: 16.09%
hth5_6: 16.09%
hth7: 2.11%
hth8_9: 16.09%
hth10: 33.31%
hth11: 2.11%
hth27: 2.11% # possible target (infant mortality)
hth28: 2.11%
hth30: 2.11% 
hth31: 2.11% # possible target (teen deaths from all causes)
hth32: 2.11%
hth33: 2.11%
'''

# health.info()
'''
Data columns (total 15 columns):
 #   Column      Non-Null Count  Dtype  
---  ------      --------------  -----  
 0   Unnamed: 0  4741 non-null   int64  
 1   LocYear     4741 non-null   str    
 2   hth1_2      4029 non-null   str    
 3   hth3_4      3978 non-null   str    
 4   hth5_6      3978 non-null   str    
 5   hth7        4641 non-null   float64
 6   hth8_9      3978 non-null   str    
 7   hth10       3162 non-null   float64
 8   hth11       4641 non-null   str    
 9   hth27       4641 non-null   float64
 10  hth28       4641 non-null   float64
 11  hth30       4641 non-null   float64
 12  hth31       4641 non-null   float64
 13  hth32       4641 non-null   float64
 14  hth33       4641 non-null   float64
dtypes: float64(8), int64(1), str(6)
memory usage: 669.9 KB
'''

# check_for_S(health)

health.replace('S', 0.10, inplace=True)
health.replace('N.A.', np.nan, inplace=True)
health.replace('N.C.', np.nan, inplace=True)

# get_percent_missing(health)


health['hth1_2'] = pd.to_numeric(health['hth1_2'])
health['hth3_4'] = pd.to_numeric(health['hth3_4'])
health['hth5_6'] = pd.to_numeric(health['hth5_6'])
health['hth8_9'] = pd.to_numeric(health['hth8_9'])
health['hth11'] = pd.to_numeric(health['hth11'])

# health.info()

# get_percent_missing(health)

imputed = health.copy()
imputed = impute(health, imputed)

# make_plots(health, imputed)

scaler = StandardScaler()
good_cols = [col for col in imputed.columns if col != 'LocYear' and col != 'hth27' and col != 'hth31']

scaled_data = scaler.fit_transform(imputed[good_cols])

scaled_df = pd.DataFrame(scaled_data, columns=good_cols, index=imputed.index)
scaled_df['LocYear'] = imputed['LocYear'] 
scaled_df['hth27'] = imputed['hth27'] 
scaled_df['hth31'] = imputed['hth31'] 

scaled_df = scaled_df[imputed.columns]

scaled_df.drop('Unnamed: 0', axis=1, inplace=True)

# print(scaled_df.head())

# make_plots(scaled_df, scaled_df)


plot_one(scaled_df, 'hth27')
plot_one(scaled_df, 'hth31')
