"""
This file is used to bring functions into the TitanicFilterGraphData.
Deals with graping data.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# import matplotlib.ticker as ticker

filename = r'C:\Users\lrb69\Documents\Python.Pandas.Files\titanic.csv'
df = pd.read_csv(filename)


def gender_graph():
    plt.title('Breakdown of the 2 Sexes')

    df.Sex.value_counts().plot(kind='pie')
    plt.show(block=True)
    plt.interactive(False)


def survived_graph():
    plt.title('0 = Dead and 1 = Survived')

    df.Survived.value_counts().plot(kind='pie')
    plt.show(block=True)
    plt.interactive(False)


def fare_age_by_gender():
    plt.title('Age vs Fare based on Class')
    sns.scatterplot(x='Age', y='Fare', hue='Pclass', data=df)
    plt.xlim(left=-2, right=83)
    plt.ylim(bottom=-3, top=530)
    plt.show(block=True)
    plt.interactive(False)


def scatter_age_survive_sex():
    plt.title('Survived vs Age based on Sex')
    sns.scatterplot(x='Survived', y='Age', hue='Sex', data=df)
    plt.show(block=True)
    plt.interactive(False)