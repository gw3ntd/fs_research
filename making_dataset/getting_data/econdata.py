import pandas as pd # type: ignore
from making_csv import clean_csv, rename_new


file_path1 = r'../excel/econ/Children in extreme poverty.xlsx'
file_path2 = r'../excel/econ/Children in families that receive public assistance.xlsx'
file_path3 = r'../excel/econ/Children in poverty.xlsx'
file_path4 = r'../excel/econ/Children living in crowded housing.xlsx'
file_path5 = r'../excel/econ/Children living in households that are owned .xlsx'
file_path6 = r'../excel/econ/Children living in households with a high housing cost burden.xlsx'
file_path7 = r'../excel/econ/Children whose parents lack secure employment.xlsx'
p7 = r'../excel/econ/p7.xlsx'
file_path8 = r'../excel/econ/Children with at least one unemployed parent.xlsx'
file_path9 = r'../excel/econ/Low-income working families with children (3).xlsx'
file_path10 = r'../excel/econ/Median family income among households with children.xlsx'
file_path11 = r'../excel/econ/Unemployment rate of parents.xlsx'
file_path12 = r'../excel/econ/Youth not attending school and not working by age group.xlsx'

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


childreninextremepov = clean_csv(file_path1, value_mapping)
childreninextremepov.rename(columns={'Data': 'econ1'}, inplace=True)
# print(childreninextremepov.head())

childreninfamsthatgetpublicassistance = clean_csv(file_path2, value_mapping)
childreninfamsthatgetpublicassistance.rename(columns={'Data': 'econ2'}, inplace=True)
# print(childreninfamsthatgetpublicassistance.head())

childreninpoverty = clean_csv(file_path3, value_mapping)
childreninpoverty.rename(columns={'Data': 'econ3'}, inplace=True)
# print(childreninpoverty.head())


childrenlivingincrowdedhousing = clean_csv(file_path4, value_mapping)
childrenlivingincrowdedhousing.rename(columns={'Data': 'econ4'}, inplace=True)
# print(childrenlivingincrowdedhousing.head())


childrenlivinginownedhomes = clean_csv(file_path5, value_mapping)
childrenlivinginownedhomes.rename(columns={'Data': 'econ5'}, inplace=True)
# print(childrenlivinginownedhomes.head())


highcostburden = clean_csv(file_path6, value_mapping)
highcostburden.rename(columns={'Data': 'econ6'}, inplace=True)
# print(highcostburden.head())

lacksecureemployment = clean_csv(file_path7, value_mapping)
df7 = clean_csv(p7, value_mapping)
lacksecureemployment = pd.concat([lacksecureemployment, df7], axis=0)
lacksecureemployment.rename(columns={'Data': 'econ7'}, inplace=True)
# print(lacksecureemployment.head())


atleast1unemp = clean_csv(file_path8, value_mapping)
atleast1unemp.rename(columns={'Data': 'econ8'}, inplace=True)
# print(atleast1unemp.head())


lowincfams = clean_csv(file_path9, value_mapping)
lowincfams.rename(columns={'Data': 'econ9'}, inplace=True)
# print(lowincfams.head())


medfaminc = clean_csv(file_path10, value_mapping, 'Currency')
medfaminc.rename(columns={'Data': 'econ10'}, inplace=True)
# print(medfaminc.head())


unemprate = clean_csv(file_path11, value_mapping)
unemprate.rename(columns={'Data': 'econ11'}, inplace=True)
# print(unemprate.head())

unempyouth = clean_csv(file_path12, value_mapping, column_name='Age group')
unempyouth.rename(columns={'16 to 19': 'econ12: 16-19',
                           "16 to 24": "econ12: 16-24",
                           "20 to 24": "econ12: 20-24"}, inplace=True)
# print(unempyouth.head())

merge_1 = pd.merge(childreninextremepov, childreninfamsthatgetpublicassistance, on='LocYear', how="outer")
print(merge_1.shape)
merge_2 = pd.merge(merge_1, childreninpoverty, on='LocYear', how="outer")
print(merge_2.shape)
merge_3 = pd.merge(merge_2, childrenlivingincrowdedhousing, on='LocYear', how="outer")
print(merge_3.shape)
merge_4 = pd.merge(merge_3, childrenlivinginownedhomes, on='LocYear', how="outer")
print(merge_4.shape)
merge_5 = pd.merge(merge_4, highcostburden, on='LocYear', how="outer")
print(merge_4.shape)
merge_6 = pd.merge(merge_5, lacksecureemployment, on='LocYear', how="outer")
print(merge_6.shape)
merge_7 = pd.merge(merge_6, atleast1unemp, on='LocYear', how="outer")
print(merge_7.shape)
merge_8 = pd.merge(merge_7, lowincfams, on='LocYear', how="outer")
print(merge_8.shape)
merge_9 = pd.merge(merge_8, medfaminc, on='LocYear', how="outer")
print(merge_9.shape)
merge_10 = pd.merge(merge_9, unemprate, on='LocYear', how="outer")
print(merge_10.shape)
merge_11 = pd.merge(merge_10, unempyouth, on='LocYear', how="outer")
print(merge_11.shape)
merge_11.to_csv('../final_csv/econ.csv')