# The code for the functions listed below are located in the TitanicInitialFxn,
# TitanicSelectingAndSlicing, TitanicFilterGraphData, and TitanicGraphData.

"""
Insights from Titanic Data Set:
1) Out of 891 people in dataset, 64.76% are male & 35.24% female.
2) In addition, 61.62% died and 35.24% survived.
3) The ages range from 0 to 80. There is only a difference of 6
years between the oldest first and third class people.
"""

try:
    # Importing files to be used that have functions inside:
    from TitanicInitialFxnTest import *
    from TitanicSelectingAndSlicing import *

    # Below function came from TitanicInitialFxnTest
    # Functions to get to know the data better
    first_last_five_rows()
    dashlinebreak()  # Function created in TitanicInitialFxnTest to print line break

    checking_col_data_types()
    dashlinebreak()

    # Below functions come from TitanicSelectingAndSlicing
    # Functions used to to select and slice data
    headandtailofnamegendersurvived()
    dashlinebreak()

    head21ofpclassandsurvived()
    dashlinebreak()

    pandaseriesgenderslice()
    dashlinebreak()

    # Importing the TitanicFilterGraphData
    from TitanicFilterGraphData import *
    # Below functions come from TitanicFilterGraphData
    # to filter and graph data
    pie_chart_gender()
    dashlinebreak()

    pie_chart_survived()
    dashlinebreak()

    class_fare_age_scatter()
    dashlinebreak()

    scatter_age_survive()
    dashlinebreak()

except (RuntimeError, NameError, SyntaxError):
    print("There is an error. Please try again.")