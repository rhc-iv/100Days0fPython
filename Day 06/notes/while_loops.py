#!/usr/bin/env python3

# ---- While Loops ----

# 'while' loops are loops that will run continuously as long
# as the condition(s) of the 'while' loop is/are true.

# Let's imagine that we have a robot that has a power cord for
# charging. Let's further imagine that the robot is currently
# plugged into an outlet in a wall (via the power cord) to
# charge up its battery. What happens if we send a message
# using Python to the robot like this:

# while plugged_in:
#     move_forward

# Well, if 'move_forward' is defined as 'Robot, move forward!',
# then our 'while' loop will run until the robot has moved so
# far forward that the plug comes out of the outlet in the wall,
# since 'plugged_in' has likely been defined as 'The power cord
# is plugged into a power source'. 'plugged_in' is only true so
# long as its definition is true. When the plug comes out of the
# outlet, the 'plugged_in' variable is no longer true so the 
# 'while' loop stops on the change in the boolean condition from
# TRUE to FALSE.

# Where 'for' loops act on lists & ranges, then stop once they
# have iterated thru those lists & ranges, 'while' loops follow
# the logic below:

# while something_is_true:
#     do something repeatedly

# In the previous exercise, we created a function that used a 
# 'for' loop to get Reeborg the Robot to jump hurdles. This 
# could also be accomplished using a 'while' loop too:

# number_of_hurdles = 6
# while number_of_hurdles > 0:
#     jump()
#     number_of_hurdles -= 1     <-- We have to deduct each hurdle from the number_of_hurdles from the
#                                    variable starting value of '6'.

# 'while' loops aren't limited to a single action within the loop;
# any action within the code block of the 'while' loop will run
# until the 'while' loop condition goes from TRUE to FALSE:

# while something_is_true:
#     do this repeatedly
#     then do this repeatedly
#     also do this repeatedly