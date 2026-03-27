import pandas as pd #type: ignore
from making_csv import clean_csv

#
p1 = r"excel/health/2-year-olds who were immunized (1).xlsx"
p2 = r"excel/health/2-year-olds who were immunized.xlsx"
#

#
p3 = r"excel/health/Births to mothers who smoked during pregnancy (1).xlsx"
p4 = r"excel/health/Births to mothers who smoked during pregnancy.xlsx"
#

#
p5 = r"excel/health/Births to mothers with less than 12 years of education .xlsx"
p6 = r"excel/health/Births to mothers with less than 12 years of education.xlsx"
#

p7 = r"excel/health/Births to unmarried women.xlsx"

#
p8 = r"excel/health/Births to women receiving late or no prenatal care 2.xlsx"
p9 = r"excel/health/Births to women receiving late or no prenatal care.xlsx"
#


p10 = r"excel/health/Child and teen death rate.xlsx"
p11 = r"excel/health/Child deaths.xlsx"
p12 = r"excel/health/Children age 18 and below without health insurance.xlsx"
p13 = r"excel/health/Children and teens with anxiety or depression.xlsx"
p14 = r"excel/health/Children who have a parent with no health insurance.xlsx"

#
p15 = r"excel/health/Children who have one or more emotional, behavioral, or developmental conditions 2.xlsx"
p16 = r"excel/health/Children who have one or more emotional, behavioral, or developmental conditions 3.xlsx"
p17 = r"excel/health/Children who have one or more emotional, behavioral, or developmental conditions.xlsx"
#

#
p18 = r"excel/health/Children who have received preventive dental care in the past year (1).xlsx"
p19 = r"excel/health/Children who have received preventive dental care in the past year.xlsx"
#

#
p20 = r"excel/health/Children whose teeth are in excellent or very good condition (1).xlsx"
p21 = r"excel/health/Children whose teeth are in excellent or very good condition.xlsx"
#

#
p22 = r"excel/health/Children with asthma problems (1).xlsx"
p23 = r"excel/health/Children with asthma problems.xlsx"
#

#
p24 = r"excel/health/Children with special health care needs (2).xlsx"
p25 = r"excel/health/Children with special health care needs.xlsx"
#

p26 = r"excel/health/High school students who felt sad or hopeless during the past year.xlsx"
p27 = r"excel/health/Infant mortality.xlsx"
p28 = r"excel/health/Low birth-weight babies.xlsx"
p29 = r"excel/health/Parents without health insurance.xlsx"
p30 = r"excel/health/Preterm births.xlsx"
p31 = r"excel/health/Teen deaths from all causes.xlsx"
p32 = r"excel/health/Total births.xlsx"
p33 = r"excel/health/Total teen births.xlsx"

value_mapping = {
    'United States': 'US',
    'Alabama': 'AL',
    'Alaska': 'AK', 
    'Arizona': 'AZ', 
    'Arkansas': 'AR', 
    'California': 'CA',
    'Colorado': 'CO', 
    'Connecticut': 'CT', 
    'Delaware': 'DE', 
    'District of Columbia': 'DC',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI', 
    'Idaho': 'ID', 
    'Illinois': 'IL',
    'Indiana': 'IN', 
    'Iowa': 'IA', 
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Puerto Rico': 'PR',
    'Rhode Island': 'RI', 
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY'
}


df1 = clean_csv(p1, value_mapping)

df2 = clean_csv(p2, value_mapping)

df1_2 = pd.concat([df1, df2], axis=0)
df1_2.rename(columns={"Data": "hth1_2"}, inplace=True)
# print(df1_2.head())


df3 = clean_csv(p3, value_mapping)

df4 = clean_csv(p4, value_mapping)

df3_4 = pd.concat([df3, df4], axis=0)
df3_4.rename(columns={"Data": "hth3_4"}, inplace=True)
# print(df3_4.head())


df5 = clean_csv(p5, value_mapping)

df6 = clean_csv(p6, value_mapping)

df5_6 = pd.concat([df3, df4], axis=0)
df5_6.rename(columns={"Data": "hth5_6"}, inplace=True)
# print(df5_6.head())


df7 = clean_csv(p7, value_mapping)
df7.rename(columns={"Data": "hth7"}, inplace=True)
# print(df7.head())


df8 = clean_csv(p8, value_mapping)

df9 = clean_csv(p9, value_mapping)

df8_9 = pd.concat([df8, df9], axis=0)
df8_9.rename(columns={"Data": "hth8_9"}, inplace=True)
# print(df8_9.head())


df10 = clean_csv(p10, value_mapping, 
                 format="Rate per 100,000")
df10.rename(columns={"Data": "hth10"}, inplace=True)
# print(df10.head())


df11 = clean_csv(p11, value_mapping, 
                 format="Number")
df11.rename(columns={"Data": "hth11"}, inplace=True)
# print(df11.head())



df12 = clean_csv(p12, value_mapping)
df12.rename(columns={"Data": "hth12"}, inplace=True)
# print(df12.head())


df13 = clean_csv(p13, value_mapping, yearmap=True)
df13.rename(columns={"Data": "hth13"}, inplace=True)
# print(df13.head())

df14 = clean_csv(p14, value_mapping)
df14.rename(columns={"Data": "hth14"}, inplace=True)
# print(df14.head())



df15 = clean_csv(p15, value_mapping, yearmap=True)

df16 = clean_csv(p16, value_mapping, yearmap=True)

df17 = clean_csv(p17, value_mapping, yearmap=True)

df151617 = pd.concat([df15, df16, df17], axis=0)
df151617.rename(columns={"Data": "hth151617"}, inplace=True)
# print(df151617.head())


df18 = clean_csv(p18, value_mapping, yearmap=True)

df19 = clean_csv(p19, value_mapping, yearmap=True)


df1819 = pd.concat([df18, df19], axis=0)
df1819.rename(columns={"Data": "hth1819"}, inplace=True)
# print(df1819.head())


df20 = clean_csv(p20, value_mapping, yearmap=True)

df21 = clean_csv(p21, value_mapping, yearmap=True)

df2021 = pd.concat([df20, df21], axis=0)
df2021.rename(columns={"Data": "hth2021"}, inplace=True)
# print(df2021.head())


df22 = clean_csv(p22, value_mapping, yearmap=True)

df23 = clean_csv(p23, value_mapping, yearmap=True)

df2223 = pd.concat([df22, df23], axis=0)
df2223.rename(columns={"Data": "hth2223"}, inplace=True)
# print(df2223.head())


df24 = clean_csv(p24, value_mapping, yearmap=True)

df25 = clean_csv(p25, value_mapping, yearmap=True)

df2425 = pd.concat([df24, df25], axis=0)
df2425.rename(columns={"Data": "hth2425"}, inplace=True)
# print(df2425.head())


df26 = clean_csv(p26, value_mapping)
df26.rename(columns={"Data": "hth26"}, inplace=True)
# print(df26.head())


df27 = clean_csv(p27, value_mapping, format="Number")
df27.rename(columns={"Data": "hth27"}, inplace=True)
# print(df27.head())

df28 = clean_csv(p28, value_mapping, format="Number")
df28.rename(columns={"Data": "hth28"}, inplace=True)
# print(df28.head())


df29 = clean_csv(p29, value_mapping)
df29.rename(columns={"Data": "hth29"}, inplace=True)
# print(df29.head())


df30 = clean_csv(p30, value_mapping)
df30.rename(columns={"Data": "hth30"}, inplace=True)
# print(df30.head())


df31 = clean_csv(p31, value_mapping, format="Number")
df31.rename(columns={"Data": "hth31"}, inplace=True)
# print(df31.head())


df32 = clean_csv(p32, value_mapping, format="Number")
df32.rename(columns={"Data": "hth32"}, inplace=True)
# print(df32.head())


df33 = clean_csv(p33, value_mapping, format="Number")
df33.rename(columns={"Data": "hth33"}, inplace=True)
# print(df33.head())

merge_1 = pd.merge(df1_2, df3_4, on='LocYear', how="outer")
print(merge_1.shape)
merge_2 = pd.merge(merge_1, df5_6, on='LocYear', how="outer")
print(merge_2.shape)
merge_3 = pd.merge(merge_2, df7, on='LocYear', how="outer")
print(merge_3.shape)
merge_4 = pd.merge(merge_3, df8_9, on='LocYear', how="outer")
print(merge_4.shape)
merge_5 = pd.merge(merge_4, df10, on='LocYear', how="outer")
print(merge_4.shape)
merge_6 = pd.merge(merge_5, df11, on='LocYear', how="outer")
print(merge_6.shape)
merge_7 = pd.merge(merge_6, df12, on='LocYear', how="outer")
print(merge_7.shape)
merge_8 = pd.merge(merge_7, df13, on='LocYear', how="outer")
print(merge_8.shape)
merge_9 = pd.merge(merge_8, df14, on='LocYear', how="outer")
print(merge_9.shape)
merge_10 = pd.merge(merge_9, df151617, on='LocYear', how="outer")
print(merge_10.shape)
merge_11 = pd.merge(merge_10, df1819, on='LocYear', how="outer")
print(merge_11.shape)
merge_12 = pd.merge(merge_11, df2021, on='LocYear', how="outer")
print(merge_12.shape)
merge_13 = pd.merge(merge_12, df2223, on='LocYear', how="outer")
print(merge_13.shape)
merge_14 = pd.merge(merge_13, df2425, on='LocYear', how="outer")
print(merge_14.shape)
merge_15 = pd.merge(merge_14, df26, on='LocYear', how="outer")
print(merge_15.shape)
merge_16 = pd.merge(merge_15, df27, on='LocYear', how="outer")
print(merge_16.shape)
merge_17 = pd.merge(merge_16, df28, on='LocYear', how="outer")
print(merge_17.shape)
merge_18 = pd.merge(merge_17, df29, on='LocYear', how="outer")
print(merge_18.shape)
merge_19 = pd.merge(merge_18, df30, on='LocYear', how="outer")
print(merge_19.shape)
merge_20 = pd.merge(merge_19, df31, on='LocYear', how="outer")
print(merge_20.shape)
merge_21 = pd.merge(merge_20, df32, on='LocYear', how="outer")
print(merge_21.shape)
merge_22 = pd.merge(merge_21, df33, on='LocYear', how="outer")
print(merge_22.shape)

merge_22.to_csv('health.csv')