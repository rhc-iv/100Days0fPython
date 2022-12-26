#!/usr/bin/env python3

# Go to http://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json for this Reeborg exercise.

# New exercise, new instructions & new conditions! First off, not only
# will the hurdles have random distances from each other, their heights
# will now be random too. A new game conditions 'wall_on_right()' has
# been introduced also & should be self-explanatory.

# This means that the 'jump()' function we created will no longer work
# because it operates off of the fact that the hurdles, whether a fixed
# distance from each other or randomly spaced apart, all have a fixed
# height. Now that both distance between & height of the hurdles is random,
# we have to implement a new approach to the game problem in order to 
# complete (solve) it successfully.

# To begin, we don't need to discard our 'jump()' function completely.
# It is still preferential to have a defined function that includes
# multiple actions, we just need to alter those actions to take the new
# rules of the game into account.
def jump():
    turn_left()

# The first action, 'turn_left()' will remain the same. This action
# is needed every time we face a hurdle in the game to orient Reeborg
# to the proper direction to begin his 'jump' over any hurdle.
    while wall_on_right:
        move()

# Since Reeborg is now oriented, we use a nested 'while' loop to check
# if the 'wall_on_right()' condition exists. As long as it does, we
# need Reeborg to 'move' in the correct direction.
    turn_right()
    move()
    turn_right()

# Once the 'wall_on_right()' condition DOES NOT exist anymore, we
# know that we have cleared the top of the hurdle and need to take
# the proper actions to go over the top of the hurdle which we defined
# in our original 'jump()' function with a combination of 'turn_right()'
# and 'move()' actions.

# Now that we have cleared a hurdle, we need Reeborg to 'move' down
# until it reaches the ground. Remember, the condition 'front_is_clear()'
# that was introduced in the previous exercise will allow Reeborg to 
# check what is in front of him; in this way, he will 'land' on the ground
# after clearing each hurdle instead of slamming into it by continuing to
# try to 'move()' past it.
    while front_is_clear:
        move()
    turn_left()

# Our newly-defined 'jump()' function has been defined. It takes into
# account all of the new conditions that exist with the random hurdle
# challenge! But, the 'at_goal()' condition still exists also, so we
# need to make sure that Reeborg stops all of his movement once he reaches
# the final flag (which is basically the 'win' condition of the game).

while not_at_goal():
    if wall_in_front(): # <-- Remember this condition exists too!!!
        jump()
    else:
        move()

# That's it! We've used an altered 'jump()' function along with multiple
# 'while' loops to account for the new conditions in the new game!