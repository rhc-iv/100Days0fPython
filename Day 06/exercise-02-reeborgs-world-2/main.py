#!/usr/bin/env python3 

# Go to https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%202&url=worlds%2Ftutorial_en%2Fhurdle2.json for this Reeborg exercise.

# This exercise introduces a new condition ('at_goal()') and new
# instructions: Have Reeborg go thru the hurdles again, but when
# it encounters a flag (the 'at_goal()' condition), have it
# stop. This is the 'win condition' for the exercise. Since the 
# race is still comprised of 6 hurdles, there's no reason to change
# our previously defined functions ('jump()'), but we do need to
# use a 'while' loop to account for the randomness of where the flag
# appears so that Reeborg stops the 'jump()' function and ends the
# race in the appropriate place.

# Until the 'at_goal()' condition appears, Reeborg should still be
# iterating thru the 'for' loop within the 'jump()' function. We'll
# make this the condition of our 'while' loop using the mathematical
# operator "!=" or 'not equal to':
while at_goal() != True: # <-- Remember 'while' loops operate on current boolean conditions
    jump() 

# We could also write this 'while' loop using 'negation' via the
# keyword 'not':
while not at_goal():
    jump()

# Notice that when we use negation, there is no need for a mathematical
# operator! Think of it like this:

# while not --condition--
#     do this

# The opposite of 'while not --condition--' is 'while condition', so the
# 'while' loop will run until the condition changes.