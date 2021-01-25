"""
This file has a list of functions used in the Titanic.Data.Visualization.py
to filter and graph data. Also, the TitanicGraphData library is imported to
provide graphs for the filtered data. Provides analysis of graphed data.
"""
# Importing files
from TitanicGraphData import *

filename = r'C:\Users\lrb69\Documents\Python.Pandas.Files\titanic.csv'
df = pd.read_csv(filename)

# After each filtering instance, brings in the corresponding graph.


def pie_chart_gender():
    print("Reshowing first 5 rows of data set:")
    print(df.head(5))

    print("\nThere are 891 people listed in the dataset.")

    print("\nNumber of males & females: (577 males and 314 females)")
    print(df['Sex'].value_counts())

    # Analysis of graph
    print("\nMales make up", round(((577 / 891) * 100), 2), "% of the dataset, while")
    print("females make up", round(((314 / 891) * 100), 2), "% of the dataset.\n")

    print("Pie chart showing males and females")

    gender_graph()  # Graph


def pie_chart_survived():
    print("\nShowing Breakdown if survived")
    print(df['Survived'].value_counts())

    # Analysis of graph
    print("\nThere are", round(((549 / 891) * 100), 2), "% of the dataset in the Titanic who")
    print("died, and", round(((314 / 891) * 100), 2), "% of the dataset who survived.\n")

    print("Pie chart showing Dead and Survived")

    survived_graph()  # Graph


def class_fare_age_scatter():
    print("\nShowing the class of the ticket based on the Fare and Age")
    # Analysis of graph
    print("\nOldest person was 80 and they were in the first class, ")
    print("while oldest person in third class was 74.")

    print("\nApproximately 75% of the people in the graph are less than 50.")
    print("Much of the data is clustered together for the second and third class.")

    print("\nScatter plot of Fare Payed and Age based on gender")
    fare_age_by_gender()  # Graph


def scatter_age_survive():
    print('\nScatter plot showing ages and if a gender survived or not')

    # Analysis of graph
    print('\nIn the dead column in 0, there appear to be more male, ')
    print('and the survived column in 1 has more ones.')

    scatter_age_survive_sex()  # Graph


def hist_embarked():
    print('Histogram of Embarked passengers')

    # Analysis of graph
    print('\nThe Titanic went from Southampton(S) to Cherbourg (C) to Queenstown (Q).')
    print('\nMore people embarked from Southampton then dropped more than one third in Cherbourg.')

    embarked_hist()  # Graph


def scatter_embark_age_class():
    print('Passenger Class based on what port entered in on and age')

    # Analysis of graph
    print("\nThe oldest first and third class passenger embarked on in Port S.")

    print('The age gap increased between passengers with each port.')

    embark_age_class()  # Graph


def scatter_age_fare_sex():
    print('Showing the gender of various passenger based on the Fare and Age')

    # Analysis of graph
    print('\nMost people below 66 paid below 50 British Pounds.')

    print('\nThe fare for both genders remains constant till age 30, when')
    print('for the males, the fare makes a wide V, while the females get a narrow V.')

    age_fare_sex_scatter()  # Graph


def scatter_age_fare_survive():
    print('Showing the survival of passengers based on the Fare and Age')

    # Analysis of graph
    print('\nThere is a general upward trend when looking at the fare and age for ')
    print('those who survived in different directions when starting at the left.')
    print('\nThe deaths form a upwards U shape around 35 to 40.')

    age_fare_survive_scatter()  # Graph


def scatter_age_fare_embark_port():
    print('Showing the embarked port for passengers based on the Fare and Age')

    # Analysis of graph
    print('\nThe fare in the passengers who embarked in Cherbourg had the biggest gap.')

    age_fare_embark_port_scatter()  # Graph
