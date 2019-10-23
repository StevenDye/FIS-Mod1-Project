""" This file contains functions used to clean datasets in FinalMod1Proj."""


def clean(data_frame, col):
    """Cleans commas and dollar signs and converts to integer"""
    data_frame[col] = data_frame[col].str.replace(',', '')
    data_frame[col] = data_frame[col].str.replace('$', '')
    data_frame[col] = data_frame[col].astype('int64')
    return data_frame.head()
