import pandas as pd # type: ignore


def clean_csv(filepath, valuemapping, format='Percent', column_name=None, yearmap=False):
    year_map = {
        '2000-2001': '2000',
        '2001-2002': '2001',
        '2002-2003': '2002',
        '2003-2004': '2003',
        '2004-2005': '2004',
        '2005-2006': '2005',
        '2006-2007': '2006',
        '2007-2008': '2007',
        '2008-2009': '2008',
        '2009-2010': '2009',
        '2010-2011': '2010', 
        '2011-2012': '2011', 
        '2012-2013': '2012', 
        '2013-2014': '2013',
        '2014-2015': '2014', 
        '2015-2016': '2015', 
        '2016-2017': '2016', 
        '2017-2018': '2017',
        '2018-2019': '2018',
        '2019-2020': '2019',
        '2020-2021': '2020', 
        '2021-2022': '2021', 
        '2022-2023': '2022',
        '2023-2024': '2023', 
        '2024-2025': '2024'
    }
    df = pd.read_excel(filepath)
    df['Location'] = df['Location'].replace(valuemapping)
    if yearmap:
        df['TimeFrame'] = df['TimeFrame'].replace(year_map)
    df['LocYear'] = df['Location'].astype(str) + df['TimeFrame'].astype(str)
    result = df[df['DataFormat'] == format].pivot_table(
        index='LocYear', 
        columns=column_name, 
        values='Data', 
        aggfunc='sum'
    )
    result.columns.name = None
    result = result.reset_index()
    return result

def rename_new(df, names, EXTRA=False):
    df.rename(columns=names, inplace=True)
    if EXTRA:
        df.drop('Total less than 18', axis=1, inplace=True)
    return df