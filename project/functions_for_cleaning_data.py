""" This file contains functions used to clean datasets in FinalMod1Proj."""

def clean(df, col):
"""Cleans commas and dollar signs, converts to integer, and returns rounded numbers in millions of dollars"""
    df[col] = df[col].str.replace(',','')
    df[col] = df[col].str.replace('$','')
    df[col] = df[col].astype('int64')
    df[col] = np.round(df[col].map(lambda x: x/1_000_000),2)
    return df.head()