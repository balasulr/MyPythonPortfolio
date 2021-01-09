"""
This file has a list of functions used in Titanic.Data.Visualization.py.
"""

import pandas as pd
filename = r'C:\Users\lrb69\Documents\Python.Pandas.Files\titanic.csv'
df = pd.read_csv(filename)
print("\nShows contents of the Excel File opened up in Pandas: \n")
print(df)


def first_last_five_rows():
    print("Shows the first & last 5 rows: \n")
    print("1. Shows first 5 rows:")
    print(df.head(5))

    print("\n2. Shows last 5 rows:")
    print(df.tail(5))


def checking_col_data_types():
    print("Checking Column Data Types")
    print("Shows Data type for each column, number of rows and columns and how many non-null values there are")

    print("\n1. Shows the Data Type for the 12 columns:")
    print("There are 5 columns that are integers and objects, "
          "and 2 columns that are floats.\n")
    print(df.dtypes)

    print("\n2. Shows how many rows and columns are in the dataset:")
    print("There are 891 rows and 12 columns.")
    print(df.shape)

    print("\n3. Shows the column data type & how many "
          "non-null values there are:\n")
    print("Age, Cabin & Embarked all have non null values, "
          "and other 9 columns have all data.")
    print("Cabin has the most non-null values (204), "
          "while Embarked has the least (889).\n")
    print(df.info())


def dashlinebreak():
    print("------------------------------------------------------------------")