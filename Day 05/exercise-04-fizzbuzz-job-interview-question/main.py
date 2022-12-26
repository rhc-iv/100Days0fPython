#!/usr/bin/env python3

# Create & store a variable for our 'for'
# loop output (with an initial value of '0'):
fizz_range = 0

# Write our 'for' loop beginning with a 
# variable name for all the list items, or
# in the case of this exercise, all of the
# number (integers) in our specified range:
for number in range(1, 101):

# Since our 'for' loop output variable is
# each iteration of the integers in our range,
# assign the output variable (fizz_range) to
# update with each iteration of integers in the
# range, expressed here in the variable 'number':
    fizz_range = number

# Use 'if/elif/else' statements to apply
# the rules of the FizzBuzz game by including
# mathematical operators (in this exercise, the
# modulo operator and the "==" operator)
#  as well as an instance of a comparison 
# operator ("and" as seen in the opening
# 'if' statement).
# Also, for each of the 'if/elif/else' statements,
# use a print() function to output the 'for'
# loop outcome of each integer in our range to
# the console. Since we want each number in
# our range to produce output, the print
# statements are indented within the 'for'
# loop in order for Python to treat them
# as nested code blocks within the 'for' loop:
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(fizz_range)