#!/usr/bin/env python3

import pandas
import random

student_dict = {
    "student": ["Jenn", "Robert", "Bruce", "Sara"],
    "score": [100, 97, 88, 90]
}
# For Loop

#   numbers = [1, 2, 3]
#   new_list = []
#   for n in numbers:
#       add_1 = n + 1
#       new_list.append(add_1)

# List Comprehension

#   new_list = [n + 1 for n in numbers]

# String as List

#   name = "Angela"
#   letters_list = [letter for letter in name]

# Range as

#   range_list = [n * 2 for n in range(1, 5)]

# Conditional List Comprehension

#   names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
#   short_names = [name for name in names if len(name) < 5]
#
#   upper_case_names = [name.upper() for name in names if len(name) > 4]

# Dictionary Comprehension

#   student_grades = {name: random.randint(1, 100) for name in names}
#   print(student_grades)
#
#   passed_students = {
#       student: grade
#       for (student, grade) in student_grades.items() if grade >= 60
#   }
#   print(passed_students)

student_data_frame = pandas.DataFrame(student_dict)
#   print(student_data_frame)

# -> .iterrows() method <-
# ------------------------

# The .iterrows() method in pandas allows us to iterate through the
# different rows of a DataFrame instead of thru each of the column.
# We use a 'for' loop to access the "index" (that is, the number that
# pandas assigns to each row) &  the "row" itself:

for (index, row) in student_data_frame.iterrows():
    # print(row)

    # Each of the rows that is returned above is a Series in pandas.

    # We can also add 'if' statements within the 'for' loop to iterate
    # thru a particular row and pull data from it. We cite the column
    # in, prepended by "row.", then use a "==" operand & then use the
    # print() function with the same "row." syntax to pull the data
    # from that row:

    if row.student == "Jenn":
        print(row.score)