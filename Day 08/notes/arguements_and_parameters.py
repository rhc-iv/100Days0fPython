#!/usr/bin/env python3

# Functions with more than 1 input:

def greet_with(name, location):
    print(f"Hello, {name}!")
    print(f"What is it like living in {location}?")

greet_with(location="Indiana", name="Robert")

# The above data within the 'greet_with' function
# call is known as "positional arguments".  That is,
# the 'greet_with' function that we defined previously
# has variables within it that are fixed; any data passed
# to those variables will occur in that specific order.
# As written, the function call would print:

#     "Hello, Robert!"
#     "What is it like living in Indiana?"

# But because those are positional arguments, if we 
# made our function call like this:

#      greet_with("Indiana", "Robert")

# then the resulting output to the console would be:

#      "Hello, Indiana!"
#      "What is it like living in Robert"

# Sure, the print statement doesn't make much sense
# contextually, but it DOES MAKE SENSE in terms of
# how Python handles positional arguments. The 2 
# arguments "Robert" and "Indiana" have switched
# places in this example, thus they will switch
# places (positions) when the function is called.

# If we want to avoid our arguments being parsed
# positionally, we can instead use what are known
# as "Positional Arguments" instead. In order to do
# this, all we have to do is use the "=" operand
# within the function call. Using the previous 
# example where we switched the arguments in the
# function call, let's amend those arguments to be
# keyword instead of positional:

#     greet_with(location="Indiana", name="Robert")

# Now when we call that function, based on the 
# arguments being passed as keywords, the output
# will look like this:

#     "Hello, Robert"
#     "What is it like living in Indiana?"
