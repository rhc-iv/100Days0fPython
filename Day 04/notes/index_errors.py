#!/usr/bin/env python3

# Index Errors occur when we apply functions or operators
# to a list, but the data sets within the list cannot return
# proper values.

# Let's say we create a list consisting of all of the states
# in the U.S. that are home to colleges in the Southeastern
# Conference.

sec = ["Alabama", "Arkansas", "Florida", "Georgia", "Kentucky", "Louisiana", "Mississippi", "Missouri", "South Carolina", "Tennessee", "Texas"]

# If we use the len() function on this list, it will return the
# number of list items.
print(len(sec))

# As we'd expect, running this code in our console produces a value
# of '11'. We also know that since list items are offset from the 
# beginning of the list, the range for the '11' list items is actually
# '0' - '10'. What would occur if we tried to index a list item that
# doesn't fall within that range? Let's see:

#   print(sec[11])
#   IndexError: list index out of range

# The code produces an IndexError message. It also tells us why the
# error occurred in our code: the index [11] is out of range of our
# list, which we know is '0' - '10'. Simple.

# Now what happens if we save the range within its own variable? Well,
# we can use the previous len() function to do that. So:
sec_schools = len(sec)

# Now let's try the print() function using the variable instead:

#   print(sec[sec_schools])
#   IndexError: list index out of range

# OH NO! It happened again! The reason that we are still seeing this
# IndexError is because the len() function returns values in integers
# not including the number '0'. So, len() return a value of '11', but
# the IndexError remains because our print() statement is using the
# returned len() value as the index, which conflicts with the way lists
# in Python are enumerated due to offset. However, we can use mathematical
# operators within the index brackets (or even within the len() function) 
# to shift the index back by 1.  Let's try it:
print(sec[sec_schools - 1])

# The output of this should be:
#    Texas
# which it is! Since indexing the list shows that Texas is '10' within
# the list's range of '0' - '10' AND because we used a mathematical
# operator (subtraction, or in this case, -1) on the index, we have
# 'shifted' the len() from '1'-'11' to be '0' - '10' with that 
# operator added.