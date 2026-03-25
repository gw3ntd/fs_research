import pandas as pd


def clean_csv(filepath, valuemapping, column_name):
    df = pd.read_excel(filepath)
    df['Location'] = df['Location'].replace(valuemapping)
    df['LocYear'] = df['Location'].astype(str) + df['TimeFrame'].astype(str)
    result = df[df['DataFormat'] == 'Number'].pivot_table(
        index='LocYear', 
        columns=column_name, 
        values='Data', 
        aggfunc='sum'
    )
    result.columns.name = None
    result = result.reset_index()
    return result

