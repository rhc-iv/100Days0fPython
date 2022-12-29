#!/usr/bin/env python3

# -> DataFrame <-
# ---------------

# A DataFrame in the pandas module is the entirety of the collection
# of data within your data file that you're working with. In this
# course section, the "weather_data.csv" file would be considered as
# a DataFrame.

# The pandas DataFrame documentation is here:
# https://pandas.pydata.org/docs/reference/frame.html

# -> Series <-
# ------------

# A Series in the pandas module is a single value set within our data
# file. So, using "weather_data.csv", if we used the following code:

# print data(["temp"])

# ...the resulting data output is a Series that shows only those
# values associated with the "temp" column in our .csv file.

# The pandas Series documentation is here:
# https://pandas.pydata.org/docs/reference/series.html

# One of the methods we can use with pandas data structures is called
# the ".to_dict" method. With this, we can take a data structure input
# and output that to a Python dictionary:

#   data = pandas.read_csv("weather_data.csv")
#   data_dict = data.to_dict()
#   print(data_dict)

# Because of the way pandas handles .csv iinput, the above code will
# result in a dictionary conversion for EACH COLUMN that it reads from
# the file.

# We can use another method in the pandas module to convert the
# individual Series into lists using the "to_list" method:

#   temp_list = date["temp"].to_list()
#   print(temp_list)

# This code will now create a Python list of items that contains all
# of the data in the "temp" column of the .csv file. Once this list
# conversion has occurred, we can now treat that list as we would any
# other list in Python. For example, if we wanted to get an AVERAGE
# TEMP VALUE of all the items in the "temp" list that we created
# using the pandas module conversion, we would code that like this:

#


