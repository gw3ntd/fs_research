import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from cleaning_funcs import get_percent_missing, check_for_NR, check_for_S, impute, make_plots

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

educ.info()