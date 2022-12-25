#!/usr/bin/env python3

# Instroduce the app per the instructions.  Here, we use
# a string.
print("Welcome to the tip calculator!")

# Use Type Conversion to convert the total bill from a
# string to an float.
bill = float(input("What was the total bill? $"))

# Use Type Conversion again to ensure that the available
# tip amounts are converted from strings to integers.
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))

# Then use Type Conversion once more to take this input
# and convert it to an integer from a string.
people = int(input("How many people to split the bill?"))

# Now that all of the input Type Conversions are finished, we
# need to define & store new variables for the mathematical
# operations needed to derive a final sum.

# The tip (converted into an integer previously) is actually
# a percentage. To express it as such, divide the integer by
# 100.  Since we are dealing with sums of money, we need to
# ensure that all of our numbers are actually floats because
# while we recognize what $1 means, the numerical representation
# of that amount is actually $1.00
tip_as_percent = tip / 100

# Once the tip percentage is calculated (and converted) it must
# be multiplied by the bill total in order to get the TOTAL amount
# of tip added to the bill.
total_tip_amount = bill * tip_as_percent

# Now that we have the total tip, we need to add it to the
# total bill to get the new sum which we will then divide
# by the number of patrons.  To do this simply add the bill amount
# to the total tip amount.
total_bill = bill + total_tip_amount

# Given the new total, we now need to calculate what the
# per-person amount is (this would be each person's share
# of the bill after the tip percentage has been added to 
# the bill).  This involves simple division: we take the
# calculated total bill (after tip percentage has been 
# included) and we divide it by the number of people who
# are going to share the bill.

bill_per_person = total_bill / people

# Since U.S. currency is calculated to the cent (from a
# value of .01 to .99), we need to ensure that the output
# of the tip calculator is expressed as a float to 2 decimal
# places. We do this by using the round() function and
# indicating within the function how man decimal places
# the rounding operation should calculate (as shown below
# by the number '2', preceeded by a comma and the variable
# before it).
final_amount = round(bill_per_person, 2)

# Now that we have performed all of the necessary calculations
# and made all of the proper Type Conversions, we can use an
# F-String (along with the final_amount variable) to print the
# output to the console without incurring Type Errors.
print(f"Each person should pay: ${final_amount}")
