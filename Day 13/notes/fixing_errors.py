#!/usr/bin/env python3

############ DEBUGGING#####################

# Fix the Errors
# Often the IDE or text editor that we use to write
# our code has built-in ways of highlighting or displaying
# errors in Python before we even attempt to run our
# code in a terminal. If we un-comment the code below,
# we'll notice that the last print statement is underlined
# in our editor as having an error. If we mouse over that
# particular line of code, we see that the logic built in
# to Python expects our print statement to be indented within
# the preceding 'if' statement. In this way, we not only
# are able to notice errors but are also given clues/hints as
# to how we can fix those errors.

#   age = input("How old are you?\n")
#   if age > 18:
#   print("You can drive at age {age}.")

# Using the error guidance given by our editor, let's correct
# the code example above so that it doesn't produce an error by
# indenting the code as specified:

#   age = input("How old are you?\n")
#   if age > 18:
#       print("You can drive at age {age}.")

# Uh-oh! Even with our correction, we still get a TypeError
# in our console output! Why? Well, notice that our input
# statement is being parsed as a string, but our 'if'
# statement is explicitly looking for an integer. Remember
# that we have to perform Type Conversions when necessary so
# that our code understands what we want. Let's try to correct
# the code by wrapping our input statement within a int()
# function:

#   age = int(input("How old are you?\n"))
#   if age > 18:
#       print("You can drive at age {age}.")

# The above correction seems to have eliminated the TypeError
# but we'll notice that our print statement still seems incorrect.
# This is because we have inserted an F-String without first
# indicating that we are even using an F-String. Let's correct
# this issue:

age = int(input("How old are you?\n"))
if age > 18:
    print(f"You can drive at age {age}.")