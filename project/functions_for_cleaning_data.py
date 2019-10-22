""" This file contains functions used to clean datasets in FinalMod1Proj."""

def clean(df, col):
    """Cleans commas and dollar signs and converts to integer"""
    import numpy as np
    df[col] = df[col].str.replace(',','')
    df[col] = df[col].str.replace('$','')
    df[col] = df[col].astype('int64')
    return df.head()

def to_millions_usd(df, col):
    import numpy as np
    df[col] = df[col].map(lambda x: x/1_000_000)
    df[col] = np.round(df[col], 2)
    return df.head()
    