#!/usr/bin/env python3

# Instead of using the print() function for
# all of our 'if/else' statements to give
# the user feedback, we need to change them
# to 'return' keywords instead to simply 
# provide a boolean value as expressed in
# the instructions for this exercise, as
# done below:
def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

# Next, we need to provide inputs for the 
# function below that we are defining. Per 
# the instructions for this exercise, we'll
# be using 'year' and 'month'.
def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# The first thing we need to do to define
# this function is to check and see if the 
# input values from the user are parsed as
# a leap year or not based on the 'is_leap'
# function above. 'If' statements are how
# we'll accomplish this:
    if month > 12 or month < 1:
        return "Invalid month."
    if is_leap(year) and month == 2:
        return 29
    return month_days[month -1]


# 🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)