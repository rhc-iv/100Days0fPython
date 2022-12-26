#!/usr/bin/env python3

# Import the random module here
import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# First, let's get the number of items on the list
# that is created from our input:
num_items = len(names)

# Next, we will apply a random selection of one
# of the items from the number of items on the
# list in the previous code. Since the len() function
# output is an integer, and we want the random
# selection to come from this group of numbers
# (integers), we will use the randint() function
# to generate that random integer, then store that
# choice within a variable.
random_choice = random.randint(0, num_items - 1)
# Since the first item of any list is indexed as
# '0', and the last item is indexed as '-1', we use
# these 2 numbers to define our range within the
# randint() function.

# Finally, we simply need to print the random choice
# to the console. However, we don't want the print()
# function to return an integer, we want it to print
# a name based on our initial input, and the number
# within the defined range that corresponds to that
# name. So before we actually run the print() function,
# we are going to take the item from the list created
# by our input (a person's name) and store that in a
# variable. We give the variable a name ('winner') then
# define & store the list item by indicating the list
# name ('names') and then taking our random variable
# ('random_choice') and indexing from the list.
winner = names[random_choice]

# Now that we have completely randomized the value that
# we want to pull from the list, we now can print the
# random variable output to the console:
print(f"{winner} is going to buy the meal today!")
