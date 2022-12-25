#!/usr/bin/env python3

# ---- Nested 'If' Statements ----
# Nested 'if' statements are code blocks that reside within
# a parent code block. They are only parsed if the parent
# block (an 'if') statment is true. If the parent block is
# is parsed by Python as false, then the nested block is 
# ignored and the program then checks the parent block's
# 'else' statment.

# Let's use our earlier rollercoaster example (used in the
# control_flow.py file) and add a nested 'if' statment to it
# where we also want to charge admission based on the age of
# the person seeking to ride the rollercoaster.
print("Welcome to the rollercoaster!!!")
height = int(input("What is your height in inches? "))

if height > 58:
    print("Congratulations! You may ride on the rollercoaster!")
    age = int(input("What is your age in years? "))
    if age <= 18:
      print("The price of admission is $7.")
    else:
      print("The price of admission is $12.")
else:
    print("Sorry, you are not tall enough to ride the rollercoaster,\ncome back later when you have grown!")

# Notice that the 'age' variable is created & stored within the
# nested 'if' statement instead of at the beginning of the program.
# Why? Because we FIRST want to determine if the person seeking to
# ride the rollercoaster is tall enough to do so.  If they are not,
# their age (and thus, the ticket price) doesn't matter. Because the
# parent 'if/else' statment would parse as FALSE, the nested 'if' 
# statment doesn't even come into effect. But if the potential rider
# is tall enough (in other words, the height input causes the boolean
# of the parent 'if/else' statement to be TRUE), then we can proceed
# to determine what their age is and, likewise, what the ticket price
# should be based on that input.

# ---- 'Elif' Statments ----
# What would we do, though, if we had multiple admission tiers; what if
# we had different prices based on age ranges instead of just two prices
# in the example above? Well, we'd use what are known as 'elif' statments.
# 'Elif' statement allow multiple boolean conditions to be checked before
# moving from an 'if' statment to its 'else' statement counterpart. Let's
# use the program from above to illustrate how 'elif' statments work:
print("Welcome to the rollercoaster!!!")
height = int(input("What is your height in inches? "))

if height > 58:
    print("Congratulations! You may ride on the rollercoaster!")
    age = int(input("What is your age in years? "))
    if age < 12:
      print("The price of admission is $5.")
    elif age <= 18:
      print("The price of admission is $7.")
    else:
      print("The price of admission is $12.")
else:
    print("Sorry, you are not tall enough to ride the rollercoaster,\ncome back later when you have grown!")

# The nested 'if' statement checks if the rider is below the
# age of 12 (and prints a price if the boolean resolves to TRUE). 
# But if the boolean value of that nested 'if' statement is FALSE, 
# instead of defaulting to the nested 'else' statment (in the 
# previous example), the 'elif' statment between the two allows 
# for another possible TRUE boolean value to be derived by checking 
# if the rider is between 12 and 18. Also, because the nested 
# 'if' statment has already been parsed (is the rider under 12?), 
# the 'elif' statment automatically calculates the age range it 
# checks as '12 to 18' since 'under the age of 12' has already 
# been checked.