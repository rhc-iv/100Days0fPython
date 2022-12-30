#!/usr/bin/env python3

import random

# -> List Comprehension <-
# ------------------------

# List Comprehension is the creation of a new list from an existing
# list. The syntax for list comprehension uses the keywords "for" and
# "in" for its basic structure. The syntax is as follows:

#   new_list =[new_item for item in list]

# Previously, we used another method to create a list from a list we
# were already working with:

#   numbers = [1, 2, 3]

#   new_list = []
#   for n in numbers:
#       add_1 = n + 1
#
#   new_list.append(add_1)
#   print(new_list)

# To accomplish the same thing above using list comprehension,
# we would do something like this:

#   new_list = [n + 1 for n in numbers]
#   print(new_list)

# We can also use list comprehension when working with list items or
# variables that are composed of strings:

#   name = "Robert"
#
#   letters_list = [letter for letter in name]
#   print(letters_list)

# Let's look at working with ranges in list comprehension. If we
# wanted to produce a list from a given range, but we wanted that
# list to be the each number in the range multiplied by 2, we could
# do the following:

#   range_list = [num * 2 for num in range(1, 5)]
#   print(range_list)

# -> Conditional List Comprehension <-
# ------------------------------------

# Conditional List Comprehension adds another keyword at the end of
# our code, "if", that is then followed by a condition. The operation
# of the code will only execute if the condition is met. Below,
# we will create a condition for our new list that will only accept
# those list items who have a character length, using the len()
# function, greater than 5:

#   names = ["Robert", "Jenn", "Bruce", "Joe", "Jessica", "Sara"]
#
#   short_names = [name for name in names if len(name) > 5]
#   print(short_names)

# We can also use function in our list comprehensions. Below,
# any name that passes the character length test will be added to a
# list, but in uppercase:

#   cap_names = [name.upper() for name in names if len(name) > 5]
#   print(cap_names)

# -> Dictionary Comprehension <-
# ------------------------------

# We can apply the same logic behind List Comprehension to
# dictionaries in Python. The syntax is the same as it would be for a
# list. If we wanted to create a new dictionary from the items in a
# list, the syntax would be as follows:

#   new_dict = {new_key:new_value for item in list}

# If we wanted to create a new dictionary from another existing
# dictionary, the syntax would change slightly:

#   new_dict = {new_key:new_value for (key, value) in dict.items()}

# As always, we can append "if (test)" to the above Comprehension in
# order to create a Conditional Dictionary based on the condition
# expressed in "(test)".

# Below, we are going to use a list & a dictionary, along with
# Comprehension to generate random scores for the names ("students")
# in our list:

names = ["Robert", "Jenn", "Bruce", "Joe", "Jessica", "Sara"]

# Our new key:value pair iterates thru each list item from "names"
# and then uses the randint() function to generate a random number
# within the range specified (here, 50-100):

student_scores = {student:random.randint(50, 100) for student in names}
# print(student_scores)

# To see how Dictionary Comprehension works on another dictionary,
# we're going to keep our code above intact; in it, we've already
# created a dictionary called "student_scores". Now we want to see,
# based on an arbitrary number, which students have "passed" based on
# the key:value pairs from that dictionary & create a new dictionary
# with those specific key:value pairs:

passed_students = {name:score for (name, score) in\
    student_scores.items()\
    if score >= 60}

print(passed_students)