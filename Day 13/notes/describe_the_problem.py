#!/usr/bin/env python3

############ DEBUGGING#####################

# # Describe Problem
# If the problem is messy & unclear in your
# head, we need to try to describe or even
# write out the issues. The below code, when
# run in our terminal, will simply print
# nothing. If we remember the class about
# the range() function, we know that the highest
# number in our range (or the 'stop') 
# does not get calculated as part of the range. 
# If we mouse over the range function, the description
# tells us that the 'stop' in a range is always
# omitted. So below, the print statement
# doesn't print anything because '20' isn't
# calculated as part of the range & our 'if' 
# statement uses the "==" operand on that
# very integer. But if we changed our range
# to (1, 21), then the print statement will
# print to the console since '20' now falls
# within the range that we have specified.

#   def my_function():
#       for i in range(1, 20):
#           if i == 20:
#               print("You got it")
#   my_function()

# Since we've described & identified the problem
# in the code above, let's re-write it to work
# as intended using our knowledge of the
# range() function:

def my_function():
    for i in range(1, 21):
        if i == 20:
            print("You got it")
my_function()
