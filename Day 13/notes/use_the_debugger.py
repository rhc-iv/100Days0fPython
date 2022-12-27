#!/usr/bin/env python3

############ DEBUGGING#####################

# Use a Debugger
# Finally, one of the tools that programmers use to
# identify & correct bugs (aka debugging) is to use
# a debugger app. Many IDEs already have debuggers
# built in, but there are also online debugging tools
# available as well, such as pythontutor.com. As well,
# there are standalone debuggers like Thonny that can
# be used for this purpose.

# If we run the below code thru a debugger, we can create
# a 'breakpoint' at any of the lines of code; that is, we 
# can tell Python to only run the code up to the breakpoint
# then return the output of the code. If we create a breakpoint
# at the 'b_list.append' function, we'll notice that instead of
# creating a list where the mutate() function is actually carrying
# out the mathematical operation that we defined in our
# 'new_item' variable, it instead is creating a single value
# and adding each one to the previous value, thus our output end
# up being a single integer that is the sum of all the values
# contained in the list we wish to mutate. As ever, if we draw
# upon our previous lessons, we know that indentation is very
# important to how Python parses code & we see that the 
# 'b_list.append' function is not indented correctly so it is
# acting as an independent line of code separate from our 'for'
# loop.

#   def mutate(a_list):
#       b_list = []
#       for item in a_list:
#           new_item = item * 2
#       b_list.append(new_item)
#       print(b_list)
#   mutate([1, 2, 3, 5, 8, 13])

# Now let's correct that indentation so that our code runs
# as we intended it to run: each integer in the list is multiplied
# by '2' and added successively to our list:

def mutate(a_list):
    b_list = []
    for item in a_list:
        new_item = item * 2
        b_list.append(new_item)
    print(b_list)
mutate([1, 2, 3, 5, 8, 13])

