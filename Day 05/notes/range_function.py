#!/usr/bin/env python3

# The range() function is quite useful (in combination
# with 'for' loops) is we want to generate a range of
# numbers or data to loop through. Below is an example
# of the syntax:

#     for number in range(a, b):
#         print(number)

# Notice that instead of our 'for' loop iterating thru
# a list, we instead define a range() that the 'for'
# loop will go thru. Let's write a 'for' loop using the
# range() function below:
for number in range(1, 10):
    print(number)
print("") # <-- For typesetting purposes only upon output
# Just because the 'for'loop is now using a range()
# instead of a list, the same rules apply:
#     1. End the 'for' loop statement with a colon (:), and
#     2. Indent any actions/functions we want to occur
#        inside the 'for' loop.

# We see that the output of our 'for' loop doesn't
# include the integer '10', even though it is the
# "end" of our range. That is because in Python, the 
# last integer in a range of numbers is not counted
# as being within the range. The output from the 
# print() function above looks like this:

#     1
#     2
#     3
#     4
#     5
#     6
#     7
#     8
#     9

# What if we wanted to print out all of the numbers
# between '1' and '10' using a 'for' loop and the
# range() function? Since only the last number in a
# range of numbers is not included in that range, we
# would simply define the range as (1, 11). The
# 'for' loop & range() function would be written
# like this:
for number in range(1, 11):
    print(number)
print("") # <-- For typesetting purposes only upon output.
# Our print statement output would now be:

#     1
#     2
#     3
#     4
#     5
#     6
#     7
#     8
#     9
#     10

# By default, the range() function iterates thru
# a range of numbers by a factor of 1. If we wanted
# to change that factor (or steps between numbers
# defined in a range), we have to alter the syntax
# as shown below:
for number in range(1, 11, 3):
    print(number)
print("") # <-- For typesetting purposes only upon output.
# The additional integer (after a 2nd comma in the
# 'for' loop) is known as the 'step'. It is how many
# places the 'for' loop will move thru the range before
# it outputs the next list item. If we are defining a
# numeric range, a good way to understand the 'step' is
# to add it to the first integer in the range (in our
# case, '1' + '3'), then add the step again to the result
# ('1' + '3' = '4'. '4' + '3' = '7', etc.). In our code,
# the output will look like this:

#     1
#     4
#     7
#     10

# What if we wanted to use a 'for' loop to calculate the
# sum of all the numbers from '1' to '100'. Similar to
# our previous 'for' loop exercises, we have to use a
# mathematical operator in a code block within the 'for'
# loop to produce the result. Since we are trying to arrive
# at a single answer, whose value has yet to be calculated,
# let's begin by creating a variable to store that final
# result. Remember, since we are looking for the sum of a
# range of numbers, our variable should not contain any number
# that would add to that range. So, we'll name it & store it
# with an initial value of '0':
total = 0

# Now let's write a 'for' loop to loop through the range
# that we've determined:
for number in range(1, 101):

# Notice here again that, since we're using a range & ranges
# in Python implicitly do not count the last number of the
# range, we have to increase our range by '1' to capture the
# range list correctly. So to ensure that '100' is also counted
# in our 'for' loop, the last number in the range needs to be
# '101'.

# Now that the 'for' loop has been made, we need to write a 
# code block that will cause the loop to add each number in the
# range to our 'total' variable, then print the output
# calculation of that mathematical operator upon the range
# we've defined:
    total += number
print(total)
