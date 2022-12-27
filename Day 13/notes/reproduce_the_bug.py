#!/usr/bin/env python3

############ DEBUGGING#####################

# Reproduce the Bug
# The code below, when run in the console, will
# occasionally print as expected. But sometimes
# it will also produce an IndexError. This is a
# difficult situation to find yourself in as a 
# programmer, especially if we've only tested the
# code briefly, assumed that it was working, then
# later on run into the bug. If we run thru each
# number of our dice_num variable, we will notice
# the IndexError occurs when we input '6' and the
# error message says 'list index our of range'. 
# Again, if we go back to our previous lesson on
# lists, we know that lists start counting from '0'
# not '1'. So 6 list items (like below) are actually
# counted as '0','1','2','3','4','5'. We also know
# that the randint() function produces a random
# number from (a, b) including both of those numbers
# specified in the range.

#   from random import randint
#   dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
#   dice_num = randint(1, 6)
#   print(dice_imgs[dice_num])

# Given the above information, let's correct the 
# code to address the bug that we reproduced by
# running each individual number thru the
# randint() function in our dice_num variable:

from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(0, 5)
print(dice_imgs[dice_num])

# Because of how list items are counted (with '0' as
# the 1st 'number' in a list), we changed our range from
# (1, 6) to (0, 5). Both ranges have a spread of 6, but
# our correction accounts for how list items get counted
# and we won't encounter any IndexErrors as a result!