#!/usr/bin/env python3

# A type of conditional statement that occurs often within
# Python programming is known as an 'if/else' statement. These
# statements describe 2 different conditions then tell Python
# what the course of action should be based on which one of the
# conditions is is true or has been met.
# Let's look at an example in the code below:
print("Welcome to the rollercoaster!!!")
height = int(input("What is your height in inches? "))

if height > 58:
    print("Congratulations! You may ride on the rollercoaster!")
else:
    print("Sorry, you are not tall enough to ride the rollercoaster,\ncome back later when you have grown!")
# Notice that if we input a value of exactly '58' in the 
# program above, the 'else' statement is returned.
# This is because the conditional operator ">" is expressly 
# for any integer 'greater than' the '58' in our 'if'
# statement. If we wanted to the cut-off for riding the
# rollercoaster to be 58 inches or above, we would use the
# ">=" conditional operator, which means 'greater than OR
# equal to' instead. See the "comparison_operators.py" file.