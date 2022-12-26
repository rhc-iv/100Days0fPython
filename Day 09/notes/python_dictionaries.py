#!/usr/bin/env python3

# Python dictionaries are very useful for grouping and
# tagging similar groups of data. There are 2 parts within
# Python dictionaries: keys (the words) and values (the
# definitions of the words):

#    KEY                             VALUE
#    Bug                             An error in a program that prevents
#                                   the program from running.
#    Function                        A piece of code that you can easily
#                                   call over and over again.
#    Loop                            The action of doing something over
#                                    and over again.

# Let's turn the above example into an actual Python
# dictionary:
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The action of doing something over and over again.",
    }

# To access information within a dictionary, we need to use
# the key to iterate the data. This is similar to using a list,
# except instead of using integers (used to represent the number
# of the list item we want to call), we use the key instead:

print(programming_dictionary["Loop"])

# A few of important points about dictionaries in Python:
#     1. Make sure that you have the spelling of the key you want
#        is correct. If the key you call within the dictionary
#        is misspelled, you will get a KeyError.
#     2. If you use a function to send a dictionary key to
#        the console, the 'value' is what will be returned, not
#        the key itself.
#     3. Ensure that the key you are calling is typed correctly
#        for whatever data type it represents. If it is an integer
#        key, don't put it in double-quotes as you would a string.

# To add new items to the dictionary later on in our code, we call 
# our dictionary name, insert a key in square brackets [], then similar
# to a variable, use the "=" operand to provide a value to this
# key. The entry will then be inserted into the dictionary:
programming_dictionary["Robert"] = "The dude typing all of this gibberish!"

# We can also create empty dictionaries that we might wish to add
# key/value pairs to later on. Simply give the new dictionary a
# name then use the "=" operand followed by an empty set of curly
# braces:
new_dictionary = {}

# The above method can also be used on existing dictionaries that 
# contain key/value pairs to 'wipe' the dictionary clean, or, empty
# it of all key/value pairs:

#     programming_dictionary = {}

# The above code would clear all data from the programming_dictionary
# dictionary.

# To edit existing entries within a Python dictionary, we use the same
# syntax format as if we were adding a new key/value pair as shown
# a few examples above:

#     programming_dictionary["Loop"] = "A continuous operation performed in Python."

# This would keep the 'Loop' key in the dictionary, but change the value
# that was originally assigned to it.

# We can loop thru a dictionary and show both the keys and the values
# with the following syntax:
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])
