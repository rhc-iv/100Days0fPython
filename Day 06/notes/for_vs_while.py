#!/usr/bin/env python3

# ---- 'For' Loops vs. 'While' Loops ----

# How do we decide on whether to use 'for' as opposed
# to 'while' loops?  For the most part, either will
# work for problem-solving using Python. A good way to
# decide is to apply the following rule-of-thumb:

#     1. 'For' loops are most useful when we want to
#         act upon each item in a list or number in a
#         range.
#     2. 'While' loops are more appropriate when we
#         want actions applied to lists, variables, or
#         ranges while a condition exists and want the
#         loop to end when that condition proves FALSE.

# 'While' loops need to be approached cautiously; unlike
# 'for' loops which have a defined 'start' and 'end' and
# will only run between those boundaries, 'while' loops 
# will run infinitely until their condition switches from
# TRUE to FALSE.

# One way we can avoid 'infinite' loops ('while' loops that
# never terminate) is to make the first action within the
# 'while' loop a print() function that contains our condition.
# Since 'while' loop operates off of the underlying boolean
# logic of our condition, then 'True' will print to our console
# after the 'while' loop starts. This can serve as a 'visual
# reminder' of the condition & give us some hint about why the
# condition remains the same and how to change that condition
# to FALSE so that the 'while' loop will eventually end.

# while 5 > 3:
#     print(5 > 3)
#     do_this_function()

# The above code will result in "True" being printed to the console
# repeatedly...5 > 3 will ALWAYS have a boolean value of TRUE. We
# need to have some other code that changes the condition to FALSE
# in order for this 'while' loop to stop.