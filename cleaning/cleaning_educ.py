import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from cleaning_funcs import get_percent_missing, check_for_NR, check_for_S, impute, make_plots
from sklearn.preprocessing import StandardScaler

educ = pd.read_csv('../making_dataset/final_csv/educ.csv')
educ = educ[~educ['LocYear'].str.contains("Alabama")]
educ = educ[educ['LocYear'].str.len() <= 6]

# get_percent_missing(educ)
'''
Unnamed: 0: 0.0%
LocYear: 0.0%
educ1: A: 52.14%
educ1: B: 52.14% 
educ1: G: 52.14%
educ1: H: 52.14%
educ1: N: 52.14%
educ2: 89.36%
educ3: IS: 89.36%
educ3: OS: 89.36%
educ4: 36.18%
educ5: 3: 73.04%
educ5: 1: 73.04%
educ5: 2: 73.04%
educ6: A: 36.18%
educ6: B: 36.18%
educ6: G: 36.18%
educ6: H: 36.18%
educ6: N: 36.18%
educ7: 1: 68.09%
educ7: 2: 68.09%
educ7: 3: 68.09%
educ7: 4: 68.09%
educ8: 1: 68.09%
educ8: 2: 68.09%
educ8: 3: 68.09%
educ8: 4: 68.09%
educ9: 1: 94.68%
educ9: 2: 94.68%
educ9: 3: 94.68%
educ9: 4: 94.68%
educ10: 1: 68.09%
educ10: 2: 68.09%
educ10: 3: 68.09%
educ10: 4: 68.09%
educ11: 1: 94.68%
educ11: 2: 94.68%
educ11: 3: 94.68%
educ11: 4: 94.68%
educ12: 1: 97.34%
educ12: 2: 97.34%
educ12: 3: 97.34%
educ12: 4: 97.34%
educ13: 70.75%
educ14: yes: 78.73%
educ14: no: 78.73%
educ15: no: 78.73%
educ15: yes: 78.73%
educ16: 3y: 9.59%
educ16: 4y: 9.59%
educ16: 5-y: 9.59%
educ16: -3y: 9.59%
educ16: tot: 9.59%
Data: 37.28%
educ18: 78.73%
educ19: 38.84%
'''

# educ.info()

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

educ.info()
'''
<class 'pandas.core.frame.DataFrame'>
Index: 1918 entries, 0 to 2781
Data columns (total 16 columns):
 #   Column       Non-Null Count  Dtype  
---  ------       --------------  -----  
 0   Unnamed: 0   1918 non-null   int64  
 1   LocYear      1918 non-null   object 
 2   educ4        1224 non-null   object 
 3   educ6: A     1224 non-null   float64
 4   educ6: B     1224 non-null   float64
 5   educ6: G     1224 non-null   float64
 6   educ6: H     1224 non-null   object 
 7   educ6: N     1224 non-null   float64
 8   educ13       561 non-null    object 
 9   educ16: 3y   1734 non-null   float64
 10  educ16: 4y   1734 non-null   float64
 11  educ16: 5-y  1734 non-null   float64
 12  educ16: -3y  1734 non-null   float64
 13  educ16: tot  1734 non-null   float64
 14  Data         1203 non-null   object 
 15  educ19       1173 non-null   float64
dtypes: float64(10), int64(1), object(5)
memory usage: 254.7+ KB
'''

educ.replace('S', 0.10, inplace=True)
educ.replace('N.A.', np.nan, inplace=True)
educ.replace('N.C.', np.nan, inplace=True)
educ.replace('<.5%', 0, inplace=True)

educ['educ4'] = educ['educ4'].astype(float)
educ['educ6: H'] = educ['educ6: H'].astype(float)
educ['educ13'] = educ['educ13'].astype(float)
educ['Data'] = educ['Data'].astype(float)


# check_for_NR(educ)
# check_for_S(educ)

imputed = educ.copy()
imputed = impute(educ, imputed)
# make_plots(educ, imputed)

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
lowkey all of these are bad except for educ16
'''