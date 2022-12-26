#!/usr/bin/env python3

# Go to https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds
# %2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en
# %2Fhurdle1.json for this Reeborg exercise.

# Use the provided functions to create & define our own function
# that will make Reeborg turn right (ignore function warnings in
# VS Code when referencing functions from the playground):
def turn_right():
    turn_left()
    turn_left()
    turn_left()


# Next, write another function (called 'jump') to use the playground
# functions along with our previously-defined 'turn_right' function
# to complete the problem presented at the above URL:
def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


# Don't forget to actually call the function!
jump()

# But since there are 6 'hurdles' in the playground, we will
# fail the challenge with just 1 call of our 'jump' function.
# We could simply type 'jump()' over & over until we reached
# the end of the challenge, but since we spent Day 5 learning
# about 'for' loops, let's combine that with our newly-created
# 'jump' function!
for step in range(6):
    jump()
