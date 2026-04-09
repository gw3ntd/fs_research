import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from cleaning_funcs import get_percent_missing, check_for_NR, check_for_S, impute, make_plots

fam = pd.read_csv('../making_dataset/final_csv/fam.csv')

fam = fam[~fam['LocYear'].str.contains("Alabama")]

# get_percent_missing(fam)

'''
Unnamed: 0: 0.0%
LocYear: 0.0%
fam1: A: 48.57%
fam1: B: 48.57%
fam1: G: 48.57%
fam1: H: 48.57%
fam1: N: 48.57%
fam4: 31.43%
fam5: 45.71%
fam7: 45.71%
fam8: 34.29%
Data_x: 77.14% # drop
Data_y: 77.14% # drop 
Data: 71.43% # drop
fam15: 31.43%
fam16: 2.86%
fam18: 82.86% # drop
fam19: 80.0% # drop
'''

fam.drop('Data_x', axis=1, inplace=True)
fam.drop('Data_y', axis=1, inplace=True)
fam.drop('Data', axis=1, inplace=True)
fam.drop('fam18', axis=1, inplace=True)
fam.drop('fam19', axis=1, inplace=True)

imputed = fam.copy()
imputed = impute(fam, imputed)
make_plots(fam, imputed)

# so actually most of the distributions look different... 
# I should look up what this means