#!/usr/bin/env python3

# By using a 'for' loop, combined with a list, we
# can go thru & perform actions on each item within
# that list. The syntax is as follows:

#     for 'item' in 'list_of_items':
#        do something with each item

# Let's try this:

fruits = ["Apple", "Banana", "Orange"]

for fruit in fruits:
    print(fruit)

# In the above example, the 'for' loop will go though
# the list and assign the variable 'fruit' to each
# item on this list & print them to the console in
# order. Essentially, 'for' loops allow us to run
# actions multiple times on the same lines of code
# in that 'for' loop. Similar to 'if/elif/else'
# statements, when we say that there is code 'IN'
# a 'for' loop, we are talking about indented code
# that is 'nested' as a code block after our 'for'
# loop has been created. NOTE: when the 'for' loop
# is written, the colon (:) must be added to it
# AND the actions we want to perform must be indented
# below it.

# In the initial 'for' loop we've created, there is only
# a single action acting upon the items in the list.
# But we can add other actions too such that each item
# on the list is interacted with or even manipulated more
# than once. Note that each action is carried out in order
# upon a list item before the 'for' loop LOOPS back to the
# list to perform those actions on the other items:
    print(fruit + " is a type fruit found in many people\'s homes.")

# If we wish to carry out a function after the 'for' loop
# but NOT within the 'for' loop itself, we simply need to
# write our functions or other code at the PREVIOUS level
# of indention so that Python understands it is not a code
# block within the preceding 'for' loop, like so:
print(fruits)