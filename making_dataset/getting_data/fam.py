import pandas as pd # type: ignore
from making_csv import clean_csv

p1 = r"../excel/family/Children by household heads educational attainment.xlsx"

p4 = r"../excel/family/Children in single-parent families.xlsx"
p5 = r"../excel/family/Children in the care of grandparents.xlsx"

p7 = r"../excel/family/Children living with cohabiting domestic partners.xlsx"
p8 = r"../excel/family/Children living with neither parent.xlsx"

p9 = r"../excel/family/Children who had a parent who was ever incarcerated 2.xlsx"
p10 = r"../excel/family/Children who had a parent who was ever incarcerated.xlsx"

p11 = r"../excel/family/Children who have experienced two or more adverse experiences 2.xlsx"
p12 = r"../excel/family/Children who have experienced two or more adverse experiences.xlsx"

p13 = r"../excel/family/Children who live in unsafe communities 2.xlsx"
p14 = r"../excel/family/Children who live in unsafe communities.xlsx"

p15 = r"../excel/family/Children who speak a language other than English at home.xlsx"
p16 = r"../excel/family/Total teen births.xlsx"

p18 = r"../excel/family/Young adults ages 18 to 24 who voted in the last midterm election.xlsx"
p19 = r"../excel/family/Young adults ages 18 to 24 who voted in the last presidential election.xlsx"

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

df1 = clean_csv(p1, value_mapping, column_name='Education Level')
df1.rename(columns={"Associate degree": "fam1: A",
                   "Bachelor's degree": "fam1: B",
                   "Graduate degree": "fam1: G",
                   "High school diploma or GED": "fam1: H",
                   "Not a high school graduate": "fam1: N"},
                   inplace=True)

# print(df1.head())


df4 = clean_csv(p4, value_mapping)
df4.rename(columns={"Data": "fam4"}, inplace=True)
# print(df4.head())


df5 = clean_csv(p5, value_mapping)
df5.rename(columns={"Data": "fam5"}, inplace=True)
# print(df5.head())


df7 = clean_csv(p7, value_mapping)
df7.rename(columns={"Data": "fam7"}, inplace=True)
# print(df7.head())

df8 = clean_csv(p8, value_mapping)
df8.rename(columns={"Data": "fam8"}, inplace=True)
# print(df8.head())

df9 = clean_csv(p9, value_mapping, yearmap=True)
# print(df9.head())
df10 = clean_csv(p10, value_mapping, yearmap=True)
# print(df10.head())
df9_10 = pd.concat([df9, df10], axis=0)
df9_10.rename(columns={"Data": "fam9_10"})
# print(df9_10.head())

df11 = clean_csv(p11, value_mapping, yearmap=True)
df12 = clean_csv(p12, value_mapping, yearmap=True)
df11_12 = pd.concat([df11, df12], axis=0)
df11_12.rename(columns={"Data": "fam11_12"})
# print(df11_12.head())


df13 = clean_csv(p13, value_mapping, yearmap=True)
df14 = clean_csv(p14, value_mapping, yearmap=True)
df13_14 = pd.concat([df13, df14], axis=0)
df13_14.rename(columns={"Data": "fam13_14"})
# print(df13_14.head())


df15 = clean_csv(p15, value_mapping)
df15.rename(columns={"Data": "fam15"}, inplace=True)
# print(df15.head())


df16 = clean_csv(p16, value_mapping, format = 'Number')
df16.rename(columns={"Data": "fam16"}, inplace=True)
# print(df16.head())

df18 = clean_csv(p18, value_mapping)
df18.rename(columns={"Data": "fam18"}, inplace=True)
# print(df18.head())


df19 = clean_csv(p19, value_mapping)
df19.rename(columns={"Data": "fam19"}, inplace=True)
# print(df19.head())

merge_1 = pd.merge(df1, df4, on='LocYear', how="outer")
print(merge_1.shape)
merge_2 = pd.merge(merge_1, df5, on='LocYear', how="outer")
print(merge_2.shape)
merge_3 = pd.merge(merge_2, df7, on='LocYear', how="outer")
print(merge_3.shape)
merge_4 = pd.merge(merge_3, df8, on='LocYear', how="outer")
print(merge_4.shape)
merge_5 = pd.merge(merge_4, df9_10, on='LocYear', how="outer")
print(merge_4.shape)
merge_6 = pd.merge(merge_5, df11_12, on='LocYear', how="outer")
print(merge_6.shape)
merge_7 = pd.merge(merge_6, df13_14, on='LocYear', how="outer")
print(merge_7.shape)
merge_8 = pd.merge(merge_7, df15, on='LocYear', how="outer")
print(merge_8.shape)
merge_9 = pd.merge(merge_8, df16, on='LocYear', how="outer")
print(merge_9.shape)
merge_10 = pd.merge(merge_9, df18, on='LocYear', how="outer")
print(merge_10.shape)
merge_11 = pd.merge(merge_10, df19, on='LocYear', how="outer")
print(merge_11.shape)
merge_11.to_csv('fam.csv')