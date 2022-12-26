#!/usr/bin/env python3

# Docstrings are ways for us to create documentation
# within our Python code while we are coding that act
# as internal 'instruction' to other programmers should
# they want to view & understand our code.

# Most IDEs contain their own built-in docstrings and
# various 3rd-party plug-in creators make docstring-type
# add-ons for different languages that are functionally
# the same thing.

# But what if we wanted to make our own docstrings to 
# be called upon within our own functions that we create?
# Below, we'll attempt to create some docstrings for a
# previous function we used. It is IMPORTANT to understand
# that within our function's code block, the docstring
# code MUST be on the first line after our function
# definition statement:
def format_name(f_name, l_name):

# Now that the function definition declaration has been
# made, we start the docstring on the following line,
# which must be indented in Python & needs to be bracketed
# within a trio of quotation marks:
    """ 
    Takes first & last name as inputs, then coverts
    and returns TitleCase versions of those inputs.
    """

# Notice that docstrings allow us to write multi-line
# strings within the same brackets. Also, once a
# docstring has been created, we will see its contents
# whenever we call our function and place the cursor
# between the function's brackets --> ()
format_name()

# The official Python documentation cautions about the
# use of multi-line comments (""" comments """) outside
# of usage as docstrings for functions. Instead, all
# non-docstring comments should be delineated with the
# '#' character.

