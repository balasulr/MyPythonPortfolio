"""
This file has a list of functions that selects and slices
data used in the Titanic.Data.Visualization.py.
"""

import pandas as pd
filename = r'C:\Users\lrb69\Documents\Python.Pandas.Files\titanic.csv'
df = pd.read_csv(filename)


def headandtailofnamegendersurvived():
    print("Shows the first 10 rows rows with their name, gender and if they survived: \n")
    print(df[['Name', 'Sex', 'Survived']].head(10))
    print("\nShows the same as above, but with the last 10 rows:")
    print(df[['Name', 'Sex', 'Survived']].tail(10))


def head21ofpclassandsurvived():
    print("Shows the first 21 rows of the ticket class, and if they survived:")
    print("\nOut of these 21 rows, there are 10 people "
          "who survived and 11 who died.")
    print(df[['Pclass', 'Survived']].head(21))


def pandaseriesgenderslice():
    print("Uses a Pandas Series to select rows using "
          "slicing to show the first 15 rows:\n")
    print("The first number is the index, then gender of the person is shown.")
    print("Out of the first 15 rows, there are 8 female and 7 male.\n")
    print(df['Sex'][0:15])