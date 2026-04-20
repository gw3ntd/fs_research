import pandas as pd # type: ignore
from making_csv import clean_csv

#
p1 = r"../excel/safety/Binge alcohol drinking among youths by age group (1).xlsx"
p2 = r"../excel/safety/Binge alcohol drinking among youths by age group (2).xlsx"
p3 = r"../excel/safety/Binge alcohol drinking among youths by age group.xlsx"
#

p4 = r"../excel/safety/Children entering foster care.xlsx"
p5 = r"../excel/safety/Children exiting foster care.xlsx"
p6 = r"../excel/safety/Children in child welfare system who have been adopted.xlsx"
p7 = r"../excel/safety/Children in foster care waiting for adoption.xlsx"

#
p9 = r"../excel/safety/Children who are confirmed by child protective services as victims of maltreatment (1).xlsx"
p10 = r"../excel/safety/Children who are confirmed by child protective services as victims of maltreatment.xlsx"
#

#
p11 = r"../excel/safety/Children who are confirmed by child protective services as victims of maltreatment by maltreatment type (1).xlsx"
p12 = r"../excel/safety/Children who are confirmed by child protective services as victims of maltreatment by maltreatment type.xlsx"
#


#
p14 = r"../excel/safety/Cigarette use in the past month by age group (1).xlsx"
p15 = r"../excel/safety/Cigarette use in the past month by age group.xlsx"
#

#
p16 = r"../excel/safety/Illicit drug use other than marijuana by age group (1).xlsx"
p17 = r"../excel/safety/Illicit drug use other than marijuana by age group (2).xlsx"
p18 = r"../excel/safety/Illicit drug use other than marijuana by age group.xlsx"
#

#
p19 = r"../excel/safety/Marijuana use by age group (1).xlsx"
p20 = r"../excel/safety/Marijuana use by age group.xlsx"
#

#
p21 = r"../excel/safety/Teens ages 12 to 17 who abused alcohol or drugs in the past year (1).xlsx"
p22 = r"../excel/safety/Teens ages 12 to 17 who abused alcohol or drugs in the past year (2).xlsx"
p23 = r"../excel/safety/Teens ages 12 to 17 who abused alcohol or drugs in the past year.xlsx"
#

p24 = r"../excel/safety/Youth residing in juvenile detention, correctional and_or residential facilities.xlsx"

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


df1 = clean_csv(p1, value_mapping, column_name='Age group',
                yearmap=True)

df2 = clean_csv(p2, value_mapping, column_name='Age group',
                yearmap=True)

df3 = clean_csv(p3, value_mapping, column_name='Age group',
                yearmap=True)


df1_2_3 = pd.concat([df1, df2, df3], axis=0)
df1_2_3.rename(columns={"12 to 17": "safe1: 1", 
                      "18 to 25": "safe1: 2"}, inplace=True)
# print(df1_2_3.head())


df4 = clean_csv(p4, value_mapping, format='Number')
df4.rename(columns={"Data": "safe4"}, inplace=True)
# print(df4.head())


df5 = clean_csv(p5, value_mapping, format='Number')
df5.rename(columns={"Data": "safe5"}, inplace=True)
# print(df5.head())


df6 = clean_csv(p6, value_mapping, format='Number')
df6.rename(columns={"Data": "safe6"}, inplace=True)
# print(df6.head())


df7 = clean_csv(p7, value_mapping, format='Number')
df7.rename(columns={"Data": "safe7"}, inplace=True)
# print(df7.head())


df9 = clean_csv(p9, value_mapping, format="Rate per 1,000")

df10 = clean_csv(p10, value_mapping, format="Rate per 1,000")


df9_10 = pd.concat([df9, df10], axis=0)
df9_10.rename(columns={"Data": "safe9_10"}, inplace=True)
# print(df9_10.head())


df11 = clean_csv(p11, value_mapping, format="Number", 
                column_name='Category')

df12 = clean_csv(p12, value_mapping, format="Number", 
                column_name='Category')


df1112 = pd.concat([df11, df12], axis=0)
df1112.drop(["Total"], axis=1, inplace=True)
df1112.rename(columns={"Emotional abuse": "safe1112: E",
                       "Medical neglect": "safe1112: M",
                       "Other/missing maltreatment type": "safe1112: O",
                       "Physical abuse": "safe1112: P",
                       "Sexual abuse": "safe1112: S"}, inplace=True)
# print(df1112.head())


df14 = clean_csv(p14, value_mapping, column_name='Age group', yearmap=True)

df15 = clean_csv(p14, value_mapping, column_name='Age group', yearmap=True)


df1415 = pd.concat([df14, df15], axis=0)
df1415.rename(columns={"12 to 17": "safe1415: 1",
                       "18 to 25": "safe1415: 2"}, inplace=True)
# print(df1415.head())


df16 = clean_csv(p14, value_mapping, column_name='Age group', yearmap=True)

df17 = clean_csv(p14, value_mapping, column_name='Age group', yearmap=True)

df18 = clean_csv(p14, value_mapping, column_name='Age group', yearmap=True)

df161718 = pd.concat([df16, df17, df18], axis=0)
df161718.rename(columns={"12 to 17": "safe161718: 1",
                       "18 to 25": "safe161718: 2"}, inplace=True)
# print(df161718.head())


df19 = clean_csv(p19, value_mapping, column_name='Age group', yearmap=True)

df20 = clean_csv(p20, value_mapping, column_name='Age group', yearmap=True)

df1920 = pd.concat([df19, df20], axis=0)
df1920.rename(columns={"12 to 17": "safe1920: 1",
                       "18 to 25": "safe1920: 2"}, inplace=True)
# print(df1920.head())



df21 = clean_csv(p21, value_mapping, yearmap=True)

df22 = clean_csv(p22, value_mapping, yearmap=True)

df23 = clean_csv(p23, value_mapping, yearmap=True)

df212223 = pd.concat([df21, df22, df23], axis=0)
df212223.rename(columns={"Data": "safe212223"}, inplace=True)
# print(df212223.head())

merge_1 = pd.merge(df1_2_3, df4, on='LocYear', how="outer")
print(merge_1.shape)
merge_2 = pd.merge(merge_1, df5, on='LocYear', how="outer")
print(merge_2.shape)
merge_3 = pd.merge(merge_2, df6, on='LocYear', how="outer")
print(merge_3.shape)
merge_4 = pd.merge(merge_3, df7, on='LocYear', how="outer")
print(merge_4.shape)
merge_5 = pd.merge(merge_4, df9_10, on='LocYear', how="outer")
print(merge_4.shape)
merge_6 = pd.merge(merge_5, df1112, on='LocYear', how="outer")
print(merge_6.shape)
merge_7 = pd.merge(merge_6, df1415, on='LocYear', how="outer")
print(merge_7.shape)
merge_8 = pd.merge(merge_7, df161718, on='LocYear', how="outer")
print(merge_8.shape)
merge_9 = pd.merge(merge_8, df1920, on='LocYear', how="outer")
print(merge_9.shape)
merge_10 = pd.merge(merge_9, df212223, on='LocYear', how="outer")
print(merge_10.shape)

merge_10.to_csv('safety.csv')