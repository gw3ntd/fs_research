import pandas as pd #type: ignore
from making_csv import clean_csv

p1 = r"excel/education/Children by household heads educational attainment.xlsx"
p2 = r"excel/education/Children who have been expelled from school.xlsx"
p3 = r"excel/education/Children who have been suspended from school.xlsx"
p4 = r"excel/education/Children who have difficulty speaking English.xlsx"
p5 = r"excel/education/Children who missed 11 or more days of school per year due to illness or injury.xlsx"
p6 = r"excel/education/Educational attainment of population ages 25 to 34.xlsx"
p7 = r"excel/education/Eighth grade math achievement levels.xlsx"
p8 = r"excel/education/Eighth grade reading achievement levels.xlsx"
p9 = r"excel/education/Eighth grade writing achievement levels.xlsx"
p10 = r"excel/education/Fourth grade math achievement levels.xlsx"
p11 = r"excel/education/Fourth grade science achievement levels.xlsx"
p12 = r"excel/education/Fourth grade writing achievement levels.xlsx"
p13 = r"excel/education/Fourth graders who are chronically absent from school.xlsx"
p14 = r"excel/education/Fourth graders who scored below proficient reading level by family income.xlsx"
p15 = r"excel/education/Fourth graders who scored below proficient reading level by school income.xlsx"
p16 = r"excel/education/Head Start enrollment by age group.xlsx"
p17 = r"excel/education/High school students not graduating on time.xlsx"
p18 = r"excel/education/Young adults ages 18 to 24 not attending school, not working, and no degree beyond high school.xlsx"
p19 = r"excel/education/Young adults ages 18 to 24 who are enrolled in or have completed college .xlsx"

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
educ_level={"Associate degree": "educ1: A", 
                    "Bachelor's degree": "educ1: B", 
                    "Graduate degree": "educ1: G",
                    "High school diploma or GED": "educ1: H",
                    "Not a high school graduate": "educ1: N"}
df1.rename(columns=educ_level, inplace=True)
# print(df1.head())

df2 = clean_csv(p2, value_mapping, format='Rate per 10,000', yearmap=True)
df2.rename(columns={"Data": "educ2"}, inplace=True)
# print(df2.head())

df3 = clean_csv(p3, value_mapping, column_name = 'Suspension Type', yearmap=True)
df3.rename(columns={"In-school": "educ3: IS", "Out-of-school": "educ3: OS"}, inplace=True)
# print(df3.head())

df4 = clean_csv(p4, value_mapping)
df4.rename(columns={"Data": "educ4"}, inplace=True)
# print(df4.head())


df5 = clean_csv(p5, value_mapping, column_name='Age group', yearmap=True)
df5.rename(columns={"12 to 17": "educ5: 3", "6 to 11": "educ5: 1", 
                    "6 to 17": "educ5: 2"}, inplace=True)
# print(df5.head())

df6 = clean_csv(p6, value_mapping, column_name='Education')
educ_level2={"Associate Degree": "educ6: A", 
                    "Bachelor's Degree": "educ6: B", 
                    "Graduate degree": "educ6: G",
                    "High school diploma or GED": "educ6: H",
                    "Not a high school graduate": "educ6: N"}
df6.rename(columns=educ_level2, inplace=True)
# print(df6.head())


df7 = clean_csv(p7, value_mapping, column_name='Achievement Level')
achieve = {
    "At or above basic": "educ7: 1",
    "At or above proficient": "educ7: 2",
    "Below basic": "educ7: 3",
    "Below proficient": "educ7: 4"
}
df7.rename(columns=achieve, inplace=True)
# print(df7.head())

df8 = clean_csv(p8, value_mapping, column_name='Achievement Level')
achieve = {
    "At or above basic": "educ8: 1",
    "At or above proficient": "educ8: 2",
    "Below basic": "educ8: 3",
    "Below proficient": "educ8: 4"
}
df8.rename(columns=achieve, inplace=True)
# print(df8.head())

df9 = clean_csv(p9, value_mapping, column_name='Achievement Level')
achieve = {
    "At or above basic": "educ9: 1",
    "At or above proficient": "educ9: 2",
    "Below basic": "educ9: 3",
    "Below proficient": "educ9: 4"
}
df9.rename(columns=achieve, inplace=True)
# print(df9.head())

df10 = clean_csv(p10, value_mapping, column_name='Achievement Level')
achieve = {
    "At or above basic": "educ10: 1",
    "At or above proficient": "educ10: 2",
    "Below basic": "educ10: 3",
    "Below proficient": "educ10: 4"
}
df10.rename(columns=achieve, inplace=True)
# print(df10.head())

df11 = clean_csv(p11, value_mapping, column_name='Achievement Level')
achieve = {
    "At or above basic": "educ11: 1",
    "At or above proficient": "educ11: 2",
    "Below basic": "educ11: 3",
    "Below proficient": "educ11: 4"
}
df11.rename(columns=achieve, inplace=True)
# print(df11.head())


df12 = clean_csv(p12, value_mapping, column_name='Achievement Level')
achieve = {
    "At or above basic": "educ12: 1",
    "At or above proficient": "educ12: 2",
    "Below basic": "educ12: 3",
    "Below proficient": "educ12: 4"
}
df12.rename(columns=achieve, inplace=True)
# print(df12.head())

df13 = clean_csv(p13, value_mapping)
df13.rename(columns={"Data": "educ13"}, inplace=True)
# print(df13.head())

df14 = clean_csv(p14, value_mapping, column_name='FamIncome')
df14.rename(columns={"Economically disadvantaged": "educ14: yes", 
                     "Not economically disadvantaged": "educ14: no"}, inplace=True)
# print(df14.head())

df15 = clean_csv(p15, value_mapping, column_name='School Income')
df15.rename(columns={"School does not receive Title I funding": "educ15: no", 
                     "School receives Title I funding": "educ15: yes"}, inplace=True)
# print(df15.head())

df16 = clean_csv(p16, value_mapping, column_name='Age group', format='Number')
df16.rename(columns={"3": "educ16: 3y", "4": "educ16: 4y", 
                     "5 years and older": "educ16: 5-y", 
                     "<3": "educ16: -3y", "Total": "educ16: tot"}, inplace=True)
# print(df16.head())

df17 = clean_csv(p17, value_mapping, yearmap=True)
df17.rename(columns={"Data": "educ17"}, inplace=True)
# print(df17.head())

df18 = clean_csv(p18, value_mapping)
df18.rename(columns={"Data": "educ18"}, inplace=True)
# print(df18.head())

df19 = clean_csv(p19, value_mapping)
df19.rename(columns={"Data": "educ19"}, inplace=True)
# print(df19.head())


merge_1 = pd.merge(df1, df2, on='LocYear', how="outer")
print(merge_1.shape)
merge_2 = pd.merge(merge_1, df3, on='LocYear', how="outer")
print(merge_2.shape)
merge_3 = pd.merge(merge_2, df4, on='LocYear', how="outer")
print(merge_3.shape)
merge_4 = pd.merge(merge_3, df5, on='LocYear', how="outer")
print(merge_4.shape)
merge_5 = pd.merge(merge_4, df6, on='LocYear', how="outer")
print(merge_4.shape)
merge_6 = pd.merge(merge_5, df7, on='LocYear', how="outer")
print(merge_6.shape)
merge_7 = pd.merge(merge_6, df8, on='LocYear', how="outer")
print(merge_7.shape)
merge_8 = pd.merge(merge_7, df9, on='LocYear', how="outer")
print(merge_8.shape)
merge_9 = pd.merge(merge_8, df10, on='LocYear', how="outer")
print(merge_9.shape)
merge_10 = pd.merge(merge_9, df11, on='LocYear', how="outer")
print(merge_10.shape)
merge_11 = pd.merge(merge_10, df12, on='LocYear', how="outer")
print(merge_11.shape)
merge_12 = pd.merge(merge_11, df13, on='LocYear', how="outer")
print(merge_12.shape)
merge_13 = pd.merge(merge_12, df14, on='LocYear', how="outer")
print(merge_13.shape)
merge_14 = pd.merge(merge_13, df15, on='LocYear', how="outer")
print(merge_14.shape)
merge_15 = pd.merge(merge_14, df16, on='LocYear', how="outer")
print(merge_15.shape)
merge_16 = pd.merge(merge_15, df17, on='LocYear', how="outer")
print(merge_16.shape)
merge_17 = pd.merge(merge_16, df18, on='LocYear', how="outer")
print(merge_17.shape)
merge_18 = pd.merge(merge_17, df19, on='LocYear', how="outer")
print(merge_18.shape)

merge_18.to_csv('educ.csv')
