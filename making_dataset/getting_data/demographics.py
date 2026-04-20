import pandas as pd # type: ignore
from making_csv import clean_csv

file_path1 = r'../excel/demographics/Child population by age group.xlsx'
file_path2 = r'../excel/demographics/Child population by gender.xlsx'
file_path3 = r'../excel/demographics/Child population by nativity (4).xlsx'
file_path4 = r'../excel/demographics/Child population by race and ethnicity.xlsx'
file_path5 = r'../excel/demographics/Children in immigrant families in which resident parents are not U.S. citizens.xlsx'
file_path6 = r'../excel/demographics/Children in immigrant families in which resident parents have been in the country five years or less.xlsx'
file_path7 = r'../excel/demographics/Children in immigrant families.xlsx'

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

childpopbyagegroup = clean_csv(file_path1, value_mapping, 'Age group')


columns={"0 to 4": "d1: 0 to 4", 
                    "12 to 14": "d1: 12 to 14", 
                    "15 to 17": "d1: 15 to 17",
                    "5 to 11": "d1: 5 to 11"}

childpopbyagegroup.rename(columns=columns, inplace=True)
childpopbyagegroup.drop('Total less than 18', axis=1, inplace=True)

# print(childpopbyagegroup.head())

#####################################################################################

childpopbygender=clean_csv(file_path2, value_mapping, 'Gender')

columns1 = {
    "Female": "d2: Female",
    "Male": "d2: Male"
}

childpopbygender.rename(columns=columns1, inplace=True)
childpopbygender.drop('Total less than 18', axis=1, inplace=True)

# print(childpopbygender.head())

#####################################################################################

childpopbynativity = clean_csv(file_path3, value_mapping, 'Nativity')

columns2 = {
    "Foreign-born": "d3: Foreign-born",
    "Native-born": "d3: Native-born"
}

childpopbynativity.rename(columns=columns2, inplace=True)

# print(childpopbynativity.head())

#####################################################################################

pd.set_option('display.max_columns', None)

columns3 = {
    "Hispanic or Latino": "d4: H or L",
    "Non-Hispanic American Indian or Alaska Native alone": "d4: AI or AN",
    "Non-Hispanic Asian alone": "d4: A",
    "Non-Hispanic Black alone": "d4: B",
    "Non-Hispanic Native Hawaiian and Other Pacific Islander alone": "d4: NH or PI",
    "Non-Hispanic Two or More Race Groups": "d4: 2 or more",
    "Non-Hispanic White alone": "d4: W"
}

childpopbyraceandethnicity = clean_csv(file_path4, value_mapping, 'Race')
childpopbyraceandethnicity.rename(columns=columns3, inplace=True)
childpopbyraceandethnicity.drop('Total less than 18', axis=1, inplace=True)
# print(childpopbyraceandethnicity.head())

#####################################################################################

# df = pd.read_excel(file_path5)
# print(df.head())

childreninimmigrantfams = clean_csv(file_path5, value_mapping, None)

childreninimmigrantfams.rename(columns={'Data': 'd5'}, inplace=True)

# print(childreninimmigrantfams.head())

#####################################################################################

merge_1 = pd.merge(childpopbyagegroup, childpopbygender, on='LocYear', how="outer")
print(merge_1.shape)
merge_2 = pd.merge(merge_1, childpopbynativity, on='LocYear', how="outer")
print(merge_2.shape)
merge_3 = pd.merge(merge_2, childpopbyraceandethnicity, on='LocYear', how="outer")
print(merge_3.shape)
merge_4 = pd.merge(merge_3, childreninimmigrantfams, on='LocYear', how="outer")
print(merge_4.shape)
merge_4.to_csv('demographics.csv') # new one without dropping missing data 