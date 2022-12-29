#!/usr/bin/env python3

# -> SLICING <-
# -------------

# Slicing is a method for extracting a portion of list items from a
# list as opposed to just accessing a single list item by itself.

piano_keys = ["a", "b", "c", "d", "e", "f", "g"]
piano_notes = ("do", "re", "mi", "fa", "so", "la", "ti")

# Let's suppose that we want to get the middle keys of this list (c,
# d, and e) in Python. We could do this by writing a 'for' loop that
# checks a condition of whether or not the iterated items is one of
# the items that we want to access. But as we know about how Python
# iterates thru list items, it doesn't actually search for the item
# itself, but rather the item's POSITION within the list that is
# expressed as an integer. We can use this knowledge to 'slice' a
# portion of the list items to access without having to create a
# 'for' loop. They syntax for slicing is simply to use square
# brackets to enter in the slice range and use a ":" character
# between the ranges of the item positions we want to slice:

# print(piano_keys[2:5])
# The above print statement acts upon the slice parameters & will
# return the following output to our console:
# ['c', 'd', 'e']

# The range of the slice that we input [2:5] corresponds to the
# position of the list items we wanted to access ['c', 'd', 'e'] and
# therefore will return or act upon those items depending on how we
# want to use the slice we create.

# Let's say we wanted to create a slice that starts at a given
# position within the list & retrieves the list items from that
# position all the way to the end of the list.  In that case, we can
# omit the second integer in our range:

# print(piano_keys[2:])
# Now our output becomes this:
# ['c', 'd', 'e', 'f', 'g']

# This process of only including one position in our slice works in
# the opposite direction as well. If we want our slice to start at
# the beginning of the list but to end at some position before the
# end of the list, then we just have to enter in an end-range integer
# within our slice with no start-point integer before the ":" character:

# print(piano_keys[:5])
# Our output then changes to:
# ['a', 'b', 'c', 'd', 'e']

# Because of the reversal of the range indicator in our slice,
# the output starts with the first list item then moves to the final
# position indicated by our slice.

# What's more, we can even add a 3rd integer to our slice that sets
# an increment, or step, for the list items. In other words, our 3rd
# number defines how many list items to SKIP OVER as our slice is
# being called.

# print(piano_keys[2:5:2])
# This output becomes:
# ['c', 'e']

# The reason that only 'c' and 'e' were returned is because our slice
# increment was set to 2. In other words, it sliced 'c' then skipped
# 2 positions of list items causing it to arrive at 'e', with the
# list item 'd' omitted form the slice.

# Continuing on with what we're able to do with slices, if we left
# our first 2 integer positions in the slice empty (but still
# included the colons) but set a final increment integer, then the
# slice will iterate thru the entire list using the increment we've set:

# print(piano_keys[::2])
# Now the output shows:
# ['a', 'c', 'e', 'g']

# The entire list has been returned in our slice, but only every 2nd
# list item due to our increment being set to 2.

# Finally, we can slice using -1 as our increment, whether our slice
# is for a range or for an entire list. The -1 integer sets the first
# returned list item as the last list item either in our slice range
# or our entire list:

# print(piano_keys[::-1])
# The displayed output:
# ['g', 'f', 'e', 'd', 'c', 'b', 'a']

# Using -1 as a slice increment, our slice always returns list items
# in the reverse order!

# -> SLICING TUPLES <-
# --------------------

# In much the same way we can use slicing on a list, we are able to
# interact with tuples using slices as well (reference the tuple at
# the beginning of the file:

# print(piano_notes[2:5]) returns:
# ['mi', 'fa', 'so']

# All of the behavior of how slices work with lists is applicable in
# the exact same way when we apply slices to tuples!