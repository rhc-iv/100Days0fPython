#!/usr/bin/env python3

# To begin, let's create a list of the 'Dirty Dozen'; a collection
# of fruits & vegetables that carry the most pesticides in them,
# even after they have been washed & peeled.
dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches",
"Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]

# As we browse thru this list, we notice the immediate relationship
# (fruits and vegetables) but since those two groups of list items
# aren't exactly the same, we can further sub-divide the list items
# into 2 smaller lists:

#     fruits[...]
#     vegetables[...]

# We could always just write 2 separate lists, but since there does
# exist a relationship between all of the main list's items, maybe
# it's possible to create one list, the somehow refine that list down
# to a particular subset of list items when we interact with the list
# in Python. This action is possible thru the use of Nested Lists.

# Going back to the above example, one of the ways we can create nested
# lists is to, in fact, create separate lists, then store them into a
# new list whose value is the combined lists.  Let's try it by splitting
# our original list between fruits & vegetables:
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

# Next, let's create a new list that includes both of them:
dirty_dozen_again = [fruits, vegetables]

# Then check for errors by printing to the console:
print(dirty_dozen_again)

# We notice a couple of things from the output:
#    1. Instead of all the fruits & vegetables being mingled
#       together like our first list, they are printed in the
#       order of how the lists are typed into the nested list
#       Brackets. Here, 'fruits' are printed out first, followed
#       by 'vegetables'.
#    2. Also notice that the output is surrounded by double-
#       brackets '[[]]'. This indicates that there is a nested
#       list in 'dirty_dozen_again' (the combination of 'fruits'
#       and 'vegetables'). In fact, each of these 'sub'-lists
#       have their own list brackets closed within the main 
#       brackets of the nested list we've created.