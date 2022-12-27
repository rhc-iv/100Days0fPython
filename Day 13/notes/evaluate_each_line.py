#!/usr/bin/env python3

############ DEBUGGING#####################

# Play Computer
# If we run the code below & we step thru it
# as we did in the previous example, we'll notice
# that there will be no print statement if we
# input either 1980 or 1994, even though both
# of those years are indicated in our code. Drawing
# upon our knowledge of 'if' statements, we know 
# that they use boolean evaluations. We also know
# that including the 'and' operation in our 'if'
# statement means that BOTH parts of it need to 
# evaluate to TRUE in order for our following 
# print() function to be executed. We know by
# way of learning about mathematical operands that
# '1980' and '1994' (as inputs) won't trigger our
# print statement because we've used the '>' and
# '<' operators. If we wanted both of those years
# to be considered & used by our print() function,
# then we need to amend the operands within our
# 'if' statement to be '>=" and "<='. Once we have
# made these corrections, then both '1980' and '1994'
# will evaluate to TRUE in our 'if' statement and the
# print() function will be executed.

#   year = int(input("What's your year of birth?\n"))
#   if year > 1980 and year < 1994:
#       print("You are a millennial.")
#   elif year > 1994:
#       print("You are a Gen Z.")

# Let's change our mathematical operands as 
# mentioned above so that both year ('1980
# & 1994) are included in our millennial print
# statement:

year = int(input("What's your year of birth?\n"))
if year >= 1980 and year <= 1994:
    print("You are a millennial.")
elif year > 1994:
    print("You are a Gen Z.")
