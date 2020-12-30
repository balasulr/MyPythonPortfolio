import pandas as pd

"""
Insights that I found about the Titanic Data
1.
"""

try:
    filename = r'C:\Users\lrb69\Documents\Python.Pandas.Files\titanic.csv'
    df = pd.read_csv(filename)
    print("\nShows contents of the Excel File opened up in Pandas: \n")
    print(df)
    print("------------------------------------------------------------------")

    print("Shows the first & last 5 rows: \n")
    print("1. Shows first 5 rows:")
    print(df.head(5))

    print("\n2. Shows last 5 rows:")
    print(df.tail(5))
    print("------------------------------------------------------------------")

    print("Checking Column Data Types")
    print("1. Shows the Data Type for the 12 columns:")
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
    print("------------------------------------------------------------------")

    print("Shows the first 10 rows rows with their name, "
          "gender and if they survived: \n")
    print(df[['Name', 'Sex', 'Survived']].head(10))
    print("\nShows the same as above, but with the last 10 rows:")
    print(df[['Name', 'Sex', 'Survived']].tail(10))
    print("------------------------------------------------------------------")

    print("Shows the first 21 rows of the ticket class, and if they survived:")
    print("\nOut of these 21 rows, there are 10 people "
          "who survived and 11 who died.")
    print(df[['Pclass', 'Survived']].head(21))
    print("------------------------------------------------------------------")

    print("Uses a Pandas Series to select rows using "
          "slicing to show the first 15 rows:\n")
    print("The first number is the index, then gender of the person is shown.")
    print("Out of the first 15 rows, there are 8 female and 7 male.\n")
    print(df['Sex'][0:15])
    print("------------------------------------------------------------------")

except (RuntimeError, NameError, SyntaxError):
    print("There is an error. Please try again.")