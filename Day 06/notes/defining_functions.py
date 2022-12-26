#!/usr/bin/env python3

# Python has a number of 'built-in' functions, which can
# be found here: https://docs.python.org/3/library/functions.html
# along with explanations. Functions give our Python apps
# and programs some sort of specific functionality. We've
# already covered some of these built-in functions, including
# the print() function and the input() function, just to name
# a few of them. 

# The print() function has a single purpose: to 'print' the
# information within () to the console. Other function like
# the len() function perform an operation on the data between
# the (); that function-manipulated data can also be saved &
# stored inside a variable or even a list.

# We can actually make our own functions! This begins by using
# the 'def' keyword; in other words, we are going to be 'defining'
# our own function. Let's make our own simple function below to
# illustrate how to incorporate 'def' into our code:

#     def my_function():
#         # Do this
#         # Then do this
#         # Finally, do this

# Let's define our own function that uses print() functions
# within it. NOTE: any functions or operations that we plan
# to use in order to define our own function must be indented
# so that they are read as a code block within our function.
# Also, the end of the 'def' statement needs to be in the
# form of a colon (":"):

#     def my_function():
#         print("Hello")
#         print("Bye")

# Since the above example doesn't require any type of input, we
# can run it in our program by typing the new function name &
# Python will execute the instructions within the new function:

#     my_function() <-- "Hello" and "Bye" are printed to the console.

# The above example is known as "calling a function". We "call"
# the function in our program whenever we need it to produce its
# content or output in our code.

# Think of defining a function as the same approach to if we were
# tasked with programming a robot. In order to get some functionality
# out of the robot, we would have to give it a set of instructions
# for singular tasks. But if we had to re-write those instructions
# for the robot on a daily basis, that would get repetitive and
# somewhat tiresome. But if we wrote those instructions, then saved
# them under a single instruction, it would be much less work to
# get the robot to do work for us. Think of defining a function as
# the same thing: instead of re-writing multiple lines of code, we
# only write those lines of code once then save them within a defined
# function for recall & use later on.