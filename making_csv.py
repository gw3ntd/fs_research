import pandas as pd


def clean_csv(filepath, valuemapping, format='Percent', column_name=None):
    df = pd.read_excel(filepath)
    df['Location'] = df['Location'].replace(valuemapping)
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