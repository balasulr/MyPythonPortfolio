import pandas as pd

"""
Key Insights that I found about the Titanic Data
1. 
"""

try:
    filename = r'C:\Users\lrb69\Documents\Python.Pandas.Files\titanic.csv'
    df = pd.read_csv(filename)
    print("Opens up Excel file and shows contents \n")
    print(df)

    print("\nViewing first & last 5 rows")
    print(df.head)
    print(df.tail)

    print("\nChecking Column Data Types")
    print("1. Shows the Data Type for the 12 columns")
    print(df.dtypes)
    print("2. Shape with showing how many rows and columns")
    print(df.shape)
    print("3. Info")
    print(df.info)


except RuntimeError:
    print("Could not open file. Please try again.")