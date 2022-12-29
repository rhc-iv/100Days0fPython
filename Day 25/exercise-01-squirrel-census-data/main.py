#!/usr/bin/env python3

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

# data = pandas.read_csv("weather_data.csv")
# temp_list = data["temp"].to_list()
# print(temp_list)

# When reading a CSV file in Python, the pandas module can also print
# our the individual columns if they are added to the print statement
# in the form of a string within a list:

# print(data["temp"])

# Another method in the pandas module is the "Series.mean" method
# that will give us the average of any series made up of integers or
# floats:


# print(data["temp"].mean())

# Another method available to us in pandas is the "Series.max" method
# that will return the maximum value of all values in a Series given
# integers or floats.

# print(data["temp"].max())

# In pandas, one of the ways that we can call sets of data within a
# column is to use a function where we insert a "." character between
# our variable ("data") and one of the columns (here, "condition").

# print(data.condition)

# Pandas also allows us to work with data within a row as opposed to
# just the columns. In a basic sense, we can specify the column via
# the previous method, then enter in the value of the row, be it a
# string, integer or otherwise using the "==" operator:

# print(data[data.day == "Monday"])

# We can also filter data by including other methods. In this
# example, we want to print the row that contains the max temp from
# the temp column along with the day & condition of that row. Again,
# we use the "==" operator but set the "filter" to be the temp
# calculated by the max() method:

# print(data[data.temp == data.temp.max()])

# So far, we've pulled entire rows from our DataFrame using pandas
# methods. But what if we wanted a single value from a specific row?
# Let's create a variable:

# monday = data[data.day == "Monday"]

# Now that the variable has been created. We can pull the explicit
# value by using the variable name ("monday") with the column type (
# "condition") to access a column type within a given row:

# print(monday.condition)

# Let's try to get the temperature for Monday in our .csv file & then
# convert it from Celsius to Fahrenheit:

# monday_temp = int(monday.temp)
# monday_temp_F = monday.temp * 9/5 + 32
# print(f"{monday_temp_F}")

# Finally, let's see how we can use the pandas module to create our
# own DataFrame from scratch. Let's begin by creating a dictionary:

# data_dict = {
#     "students": ["Robert", "Jenn", "Tom"],
#     "scores": [90, 97, 85]
# }

# Now we call the pandas module & use the DataFrame class to convert
# our dictionary to a DataFrame:

# data = pandas.DataFrame(data_dict)
# print(data)

# Since we're already working with a .csv file for this class
# section, let's look at how we can use the pandas module to convert
# our already-created dictionary into a .csv file. We can accomplish
# this using the "to_csv" method available in the module. It takes
# only a single argument, which is the filename & path that we want to
# save the
# .csv file to:

# data.to_csv("new_data.csv")

# -> Squirrel Census Data Analysis <-
# -----------------------------------

# For this exercise, we want to start by pulling all of the data from
# the "Primary Fur Color" column in the .csv file and also getting a
# count for each of the value types in that column:

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_"
                       "Data.csv")

gray_squirrels_count = len(data["Primary Fur Color"] == "Gray")
cinnamon_squirrels_count = len(data["Primary Fur Color"] == "Cinnamon")
black_squirrels_count = len(data["Primary Fur Color"] == "Black")

# Next, we're going to use this information to create a dictionary:

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels_count,
              cinnamon_squirrels_count,
              black_squirrels_count,
              ]
}

# Now that we have a dictionary that contains the extracted values,
# we are going to convert this dictionary into a DataFrame:

df = pandas.DataFrame(data_dict)

# Finally, once the DataFrame has been created, we will now convert
# that DataFrame into its own .csv file with the contents we
# originally extracted from the initial .csv file:

df.to_csv("squirrel_count.csv")