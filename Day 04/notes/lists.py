#!/usr/bin/env python3

# A list in Python is a type of data structure: it is a
# protocol to create & store data within our code.
# Another type of data structure that we are already
# familiar with is the variable. Whereas a variable stores
# a single piece of data, lists allow us to store grouped
# (or multiple) pieces of data (which typically have some
# relationship to each other). Lists also allow us to
# control the order of the information stored within
# them. Finally, lists can store mixed data types!
# At their most basic, lists look like variables,
# but with multiple items assigned to them, held between
# two square brackets '[]' and separated by commas.

#    fruit = [item1, item2]
#    WARNING: List "item1" is not defined.

# Note that in the list above, we get a warning message in
# Python that the items within the list are not defined.
# As a list is a DATA structure, that means that we must
# fill the list with data types AND those data types must
# be syntactically correct! The warning above occurs because
# the items can only be parsed as strings if they are inside
# double-quotes. Otherwise, in our example, Python reads
# the items as code and tries to parse them as such. Let's
# try again!

#    fruit = ["item1", "item2"]

# Hooray! The warning dialog has now disappeared because
# Python now sees the list items (the data inside the
# list) as strings!

# We can do different types of operations using lists. One 
# simple interaction is that instead of printing an entire
# list to the console, we can instead extract items from a
# list by indexing (using []) an item number or a range 
# of items within the print() function.
fruit = ["item1", "item2", "item3", "item4"]
print(fruit[2])
# In this example, [2] in the print() function will print
# "item3". Remember: the number within the index brackets
# delineates the OFFSET from the beginning of the list, not
# the "number" of the item in the order of the list which
# is how we typically would assign numbers to those items.
# So, "item3" is offset from the beginning of the list (the
# 'beginning being "item1") by 2 places. "Item1" is indexed
# as [0] because it is at the beginning of the list and thus
# does not have an offset.

# List indexing also responds to negative number input;
# starting with [-1], the index will count backwards from
# the end of the list (there is no [-0], so we don't use
# it). Either indexing method can be used to print the list
# item to the console. NOTE: an indexed item from a list
# can also be saved & stored inside of a variable.
print(fruit[-1])
# In this example, the print statement will be "item4" since
# it is the last item in the list.

# We can manipulate list items by indexing an item within
# the list (not necessarily using a print() function). This
# is very similar to creating a variable; see below:
fruit[1] = "changed_item"
print(fruit)
# After printing to the console, we now see that we have
# changed "item2" into "changed_item".

# If we wanted to add an item to the list, we could use
# the append() function, which will add the input to the
# end of the list.
fruit.append("item5")
print(fruit)

# Another function we can use within lists is the extend()
# function. This will add multiple items to the end of the
# existing list by creating another list then appending it
# to our current list. This is the syntax that we would use
# to do that:
fruit.extend(["item6", "item7", "item8", "item9", "item10"])
print(fruit)

# The official Python documents at docs.python.org explain
# other functions that can be used when working with lists.