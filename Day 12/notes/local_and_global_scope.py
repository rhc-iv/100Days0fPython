#!/usr/bin/env python3

# Local scope exists within functions. 
def drink_potion():
    potion_strength = 2
    print(potion_strength)
drink_potion()

# The above code, when the function is
# called, prints like you'd expect it to
# print: '2'. But since the variable
# 'potion_strength' has been defined INSIDE
# the 'drink_potion' function, it doesn't
# exist outside of that function; in other
# words, Python will give a NameError if
# we did this outside of 'drink_potion':

#     print(potion_strength)

# Why? It is because the variable has
# been created & stored within its own
# function & only interoperates with the
# program whenever the function is called.
# Thus, LOCAL SCOPE means that the particular
# code is ONLY VALID in Python when its
# parent code (think: function -> code block)
# is called.

# There is another type of scope called
# GLOBAL SCOPE, which is variables or functions
# that are defined outside of any other variable
# or function and are parsed by Python anytime
# they are called. This is known as 'top-level'
# code: it isn't indented below a parent line
# or lines of code that would cause it to be
# treated with LOCAL SCOPE.

# Global variables, by the way, are available
# both inside & outside of functions once they
# have been created & stored.