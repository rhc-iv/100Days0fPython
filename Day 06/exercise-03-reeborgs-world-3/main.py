#!/usr/bin/env python3

# Go to https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%203&url=worlds%2Ftutorial_en%2Fhurdle3.json for this Reeborg exercise.

# Now the race course has changed: the hurdles are not
# the same distance away; they are now random. So our
# jump() function will end in a failure. THe exercise
# provides a few new conditions:

#     1. 'front_is_clear()' <-- There is nothing in front of whatever direction Reeborg
#                               is facing
#     2. 'wall_in_front()'  <-- There is a wall in front of whatever direction Reeborg
#                               is facing.

# The previous 'at_goal()' function, which means that Reeborg
# should cease all actions is also still present in this 
# exercise.

# Since the condition 'at_goal()' is our 'win' condition, we
# will open with a 'while' loop that is the opposite of that
# condition:
while not at_goal():

# We will use an 'if' statement to check if the first new
# condition exists and what actions to take if it does or
# if it doesn't:
    if wall_in_front():

# The above code tests if 'wall_in_front()' is TRUE. If it is,
# like previously, we want to invoke the 'jump()' function that
# we created before:
        jump()

# But the 'while' loop will fail using the above code
# because the first action in our 'jump()' function is to
# 'move()'. Since 'wall_in_front()' can be TRUE, the 
# 'move()' function within our created 'jump()' function
# will cause Reeborg to run into the wall before jumping
# over it, which is a 'fail' condition for the game. So,
# in this exercise, we need modify our 'jump()' function
# so that the first action within it is the 'turn_left()'
# function which will orient Reeborg in the correct 
# direction to avoid running into the wall!
def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

# This alteration of the 'jump()' function (combined with
# our previously-defined function, 'turn_right()'), will
# cause the 'while' loop to operate correctly. All 3 of
# the game conditions: 'front_is_clear()', 'wall_in_front()'
# and 'at_goal()' are accounted for & the appropriate action
# to take when one of them is encountered are addressed in
# the 'if/else' statement in our 'while' loop.
