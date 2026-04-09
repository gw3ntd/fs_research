import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from cleaning_funcs import get_percent_missing, check_for_NR, check_for_S, impute, make_plots

demo = pd.read_csv('../making_dataset/final_csv/demographics.csv')
demo = demo[~demo['LocYear'].str.contains("Alabama")]

get_percent_missing(demo)