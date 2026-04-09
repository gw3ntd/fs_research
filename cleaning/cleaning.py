import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


safe = pd.read_csv('../making_dataset/final_csv/safety.csv')

# print(safe.head())


def get_percent_missing(df):
    for column in df:

        # Select column contents by column
        # name using [] operator
        missing = df[column].isnull().sum() / len(df)
        missing = missing * 100
        print(f"{column}: {round(missing, 2)}%")

'''
Percent of missing values per column

LocYear: 0.0
safe1: 1: 0.2
safe1: 2: 0.2
safe4: 0.029131652661064426
safe5: 0.02857142857142857
safe6: 0.22857142857142856
safe7: 0.02857142857142857
safe9_10: 0.0
safe1112: E: 0.02857142857142857
safe1112: M: 0.02857142857142857
Neglect: 0.02857142857142857
safe1112: O: 0.02857142857142857
safe1112: P: 0.02857142857142857
safe1112: S: 0.02857142857142857
safe1415: 1: 0.6571428571428571
safe1415: 2: 0.6571428571428571
safe161718: 1: 0.6571428571428571
safe161718: 2: 0.6571428571428571
safe1920: 1: 0.17142857142857143
safe1920: 2: 0.17142857142857143
safe212223: 0.2857142857142857
'''

safe.drop('safe1415: 1', axis=1, inplace=True)
safe.drop('safe1415: 2', axis=1, inplace=True)
safe.drop('safe161718: 1', axis=1, inplace=True)
safe.drop('safe161718: 2', axis=1, inplace=True)

# safe.info()
'''
<class 'pandas.DataFrame'>
RangeIndex: 1785 entries, 0 to 1784
Data columns (total 18 columns):
 #   Column       Non-Null Count  Dtype  
---  ------       --------------  -----  
 0   Unnamed: 0   1785 non-null   int64  
 1   LocYear      1785 non-null   str    
 2   safe1: 1     1428 non-null   float64
 3   safe1: 2     1428 non-null   float64
 4   safe4        1733 non-null   float64
 5   safe5        1734 non-null   float64
 6   safe6        1377 non-null   float64
 7   safe7        1734 non-null   str    
 8   safe9_10     1785 non-null   str    
 9   safe1112: E  1734 non-null   str    
 10  safe1112: M  1734 non-null   str    
 11  Neglect      1734 non-null   str    
 12  safe1112: O  1734 non-null   str    
 13  safe1112: P  1734 non-null   str    
 14  safe1112: S  1734 non-null   str    
 15  safe1920: 1  1479 non-null   float64
 16  safe1920: 2  1479 non-null   float64
 17  safe212223   1275 non-null   float64
dtypes: float64(8), int64(1), str(9)
memory usage: 307.1 KB
'''

def check_for_S(df):
    for column in df:

        # Select column contents by column
        # name using [] operator
        S = df[column].isin(['N.R.']).any()
        print(f"{column}: {S}")

# check_for_S(safe)

safe.replace('N.R.', np.nan, inplace=True)
safe.replace('N.A.', np.nan, inplace=True)

# get_percent_missing(safe)
'''
I changed the function to show percentages

Unnamed: 0: 0.0%
LocYear: 0.0%
safe1: 1: 20.0%
safe1: 2: 20.0%
safe4: 2.91%
safe5: 2.86%
safe6: 22.86%
safe7: 2.91%
safe9_10: 8.68%
safe1112: E: 16.75%
safe1112: M: 29.47%
Neglect: 11.54%
safe1112: O: 55.13%
safe1112: P: 11.6%
safe1112: S: 11.54%
safe1920: 1: 17.14%
safe1920: 2: 17.14%
safe212223: 28.57%
'''

safe.drop('safe1112: O', axis=1, inplace=True)

safe['safe7'] = pd.to_numeric(safe['safe7'])
safe['safe9_10'] = pd.to_numeric(safe['safe9_10'])
safe['safe1112: E'] = pd.to_numeric(safe['safe1112: E'])
safe['safe1112: M'] = pd.to_numeric(safe['safe1112: M'])
safe['safe1112: P'] = pd.to_numeric(safe['safe1112: P'])
safe['safe1112: S'] = pd.to_numeric(safe['safe1112: S'])
safe['Neglect'] = pd.to_numeric(safe['Neglect'])

# safe.info()

'''
<class 'pandas.DataFrame'>
RangeIndex: 1785 entries, 0 to 1784
Data columns (total 17 columns):
 #   Column       Non-Null Count  Dtype  
---  ------       --------------  -----  
 0   Unnamed: 0   1785 non-null   int64  
 1   LocYear      1785 non-null   str    
 2   safe1: 1     1428 non-null   float64
 3   safe1: 2     1428 non-null   float64
 4   safe4        1733 non-null   float64
 5   safe5        1734 non-null   float64
 6   safe6        1377 non-null   float64
 7   safe7        1733 non-null   float64
 8   safe9_10     1630 non-null   float64
 9   safe1112: E  1486 non-null   float64
 10  safe1112: M  1259 non-null   float64
 11  Neglect      1579 non-null   float64
 12  safe1112: P  1578 non-null   float64
 13  safe1112: S  1579 non-null   float64
 14  safe1920: 1  1479 non-null   float64
 15  safe1920: 2  1479 non-null   float64
 16  safe212223   1275 non-null   float64
dtypes: float64(15), int64(1), str(1)
memory usage: 247.7 KB
'''


def impute(og, new):
    for column in og:
        if og[column].dtype == 'float64':
            median = og[column].median()
            new[column] = new[column].fillna(median)
    return new
    
imputed = safe.copy()
imputed = impute(safe, imputed)

# print(imputed.head())

# imputed.info()

def comp_dist(og, new, column):

    fig = plt.figure()
    ax = fig.add_subplot(111)

    # original variable distribution
    og[column].plot(kind='kde', ax=ax)

    # variable imputed with the median
    new[column].plot(kind='kde', ax=ax, color='red')

    lines, labels = ax.get_legend_handles_labels()
    ax.legend(lines, labels, loc='best')

    plt.show()

def make_plots(og, new):
    for column in og:
        if og[column].dtype == 'float64':
            comp_dist(og, new, column)



# make_plots(safe, imputed)

# filtered_df = imputed[imputed['LocYear'].str.contains('-', na=False)]
# print(filtered_df)

