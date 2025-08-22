"""
`common.py`

Shared utility functions for the rice yield prediction project.

This module contains general-purpose cleaning functions that are reused across 
multiple data processing scripts, such as:
- Reading and saving CSV files
- Dropping unneeded location identifier columns
- Standardizing district names to present-day naming conventions
- Normalizing column names to lowercase, snake_case

These functions ensure consistency and reduce duplication in the preprocessing pipeline.
"""

import pandas as pd

district_names = {'Chengalpattu MGR Kancheepuram': 'Kancheepuram',
                  'Tiruchirapalli Trichy': 'Tiruchirappalli',
                  'Periyar(Erode)': 'Erode',
                  'Dindigul Anna': 'Dindigul',
                  'Virudhunagar Kamarajar': 'Virudhunagar',
                  'Sivagangai Pasumpon': 'Sivagangai',
                  'Chidambanar Toothukudi': 'Thoothukudi',
                  'North Arcot Vellore': 'Vellore',
                  'South Arcot Cuddalore': 'Cuddalore',
                  'Tiruvarur': 'Thiruvarur',
                  'Thiruppur': 'Tiruppur',
                  'Thiruvannamalai': 'Tiruvannamalai'}

def read_csv(path: str) -> pd.DataFrame:
    """ Returns a `DataFrame` object"""
    return pd.read_csv(path)

def write_csv(df: pd.DataFrame, path: str) -> None:
    """ Creates a `csv` file on the `path` by converting a `DataFrame` object """
    df.to_csv(path, index=False)

def drop_location_id(df: pd.DataFrame) -> pd.DataFrame:
    """ Drops the location identifiers and returns the `DataFrame` object"""
    return df.drop(columns=['Dist Code', 'State Code', 'State Name'], inplace=False)

def update_district_names(df: pd.DataFrame) -> pd.DataFrame:
    """ Updates the old district names to present-day names"""
    return df.replace(district_names, inplace=False)

def rename_column(column: str) -> str:
      return column.replace(' ', '_').replace('(', '').replace(')', '').lower()

def map_columns(df: pd.DataFrame) -> pd.Index:
    """ Maps the column names with the function `rename_column`"""
    return df.columns.map(lambda col: rename_column(col))

def infer_column_name(file_name: str) -> str:
    """ Removes the extension in file name to be used as a column name """
    return file_name.replace(".csv", '')

def infer_output_name(file_name: str) -> str:
    """ Returns the output file_name given the column name """
    return f"cleaned_{file_name}" 

def annual_average(df: pd.DataFrame, column_name: str) -> pd.DataFrame:
    monthly_cols = df.columns.difference(['year', 'dist_name'])
    df[column_name] = df[monthly_cols].mean(axis=1).round(2)
    return df[['year', 'dist_name', column_name]]


if __name__ == "__main__":
    print(__doc__)