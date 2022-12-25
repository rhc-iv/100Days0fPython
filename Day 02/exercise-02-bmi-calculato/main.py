#!/usr/bin/env python3

# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

# We need to do Type Conversions of the initial input values.  The
# input asks for values expressed as strings; we convert height to a
# float and we convert weight to an integer.  After the conversion,
# we store both values inside of new variables.

conv_height = float(height)
conv_weight = int(weight)

# Finally, we have to arrange the values using mathematical
# operations according to how BMI is calculated.  The calculation
# calls for weight divided by height-squared.  After this operation
# has been written, we have to convert it to an integer (whole
# number) as the output.  This is accomplished with the int()
# function in order to convert the data type correctly (which would
# otherwise print as a float).  Finally, the print() function prints
# the output to the console.

print(int(conv_weight / (conv_height * conv_height)))

# Instructor's Solution:
#     The program could also be written as below.
# ============================================
# =  bmi = int(weight) / float(height) ** 2  =
# =  bmi_as_int = int(bmi)                   =
# ============================================
