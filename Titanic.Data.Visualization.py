# The code for the functions listed below are located in the
# TitanicInitialFxn and TitanicSelectingAndSlicing files.

try:
    # Bringing in files here & both files contain pandas
    # which is used to perform the data visualization
    from TitanicInitialFxnTest import *
    from TitanicSelectingAndSlicing import *
    dashlinebreak()  # Function created in
    # TitanicInitialFxnTest to print line break

    # Below functions come from TitanicInitialFxnTest
    # Functions to get to know the data better
    firstlast()
    dashlinebreak()

    checkingcoldatatypes()
    dashlinebreak()

    # Below functions come from TitanicSelectingAndSlicing
    # Functions used to to select and slice data
    headandtailofnamegendersurvived()
    dashlinebreak()

    head21ofpclassandsurvived()
    dashlinebreak()

    pandaseriesgenderslice()
    dashlinebreak()

except (RuntimeError, NameError, SyntaxError):
    print("There is an error. Please try again.")