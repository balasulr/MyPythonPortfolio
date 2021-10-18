"""
This file is a separate file from the Titanic.Data.Visualization.py
file and is used to show Exception Handling with the Titanic Data set.

I have added some additional graphs with some insight below.

The last graph is a graph that I am pretending to pull from the
TitanicGraphData file and did not actually import the file into
this sheet as a way to show that an error message shows up.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def dash_linebreak():
    print("----------------------------------------------------------------------")


filename = r'C:\Users\lrb69\Documents\Python.Pandas.Files\titanic.csv'
df = pd.read_csv(filename)

dash_linebreak()
print("This file showcases Exeception Handling as related to the Titanic Data set.")
dash_linebreak()


def class_pie_graph():
    plt.title('Breakdown of the Classes aboard the Titanic')

    df.Pclass.value_counts().plot(kind='pie')
    plt.show(block=True)
    plt.interactive(False)


def embarked__pie_graph():
    plt.title('Breakdown of the ports that people entered the Titanic from')

    df.Embarked.value_counts().plot(kind='pie')
    plt.show(block=True)
    plt.interactive(False)


try:
    print("Pie Chart showing that a majority of the passengers aboard the Titanic were third class:")
    dash_linebreak()
    class_pie_graph()

    print("Pie Chart showing that what ports passengers entered the Titanic:")
    dash_linebreak()
    embarked__pie_graph()

    print("The below is an example of purposely putting in an error message:")
    print("\nHere, I am pulling the Gender graph from the TitanicGraphData file.")
    print("\nFor this graph, I could have forgotten to import the data that was to be used.")
    # The line to import the TitanicGraphData file is:
    # from TitanicGraphData import *
    # Can uncomment the above line to have the graph show:
    dash_linebreak()
    gender_graph()

except NameError as err:
    print("There is an error. Please try again.\n")
    print('Handling run-time error:', err)
    dash_linebreak()
