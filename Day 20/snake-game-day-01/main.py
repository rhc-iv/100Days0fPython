#!/usr/bin/env python3

from turtle import Turtle, Screen

# We will import the 'time' module to have access to methods that
# will allow us to slow down the 'snake segments' as the game is
# being played on the screen:

import time

# Since we have created a separate snake.py file which will act as
# our Snake class, we have to import it as well:

from snake import Snake

# The first thing we're going to do is to create a new screen which
# is basically the window in which the game will take place. We are
# going to use the .setup() method to define the size of the screen (
# using keyword arguments), we're going to use the .bgcolor() method
# to make the background of the screen black and we are going to use
# the .title() method to give a title to the screen. As ever, at the
# bottom of our code, we are also going to call the .exitonclick()
# method so that the screen remains open until we click it with our
# mouse:

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

# We want to keep each individual turtle instance (or, in this case,
# snake segment) from being disconnected to the others in its
# animation. We can use the .tracer() method to do this by setting it
# to '0' per the turtle module documentation:

screen.tracer(0)

# Now that our new Snake class has been imported, we're going to
# create a new object based on that class. Any time this object is
# called, it will trigger the __init__ attributes & methods that were
# created in the snake.py file:

snake = Snake()

# We are going to create the body of the snake using the turtle
# module by initially creating 3 consecutive squares lined up next to
# each other horizontally:

# segment_1 = Turtle(shape="square")
# segment_1.color("white")
# segment_2 = Turtle(shape="square")
# segment_2.color("white")
# segment_2.goto(x=-20, y=0)
# segment_3 = Turtle(shape="square")
# segment_3.color("white")
# segment_3.goto(x=-40, y=0)

# An easier way of achieving this result without typing in all of the
# code above would be to iterate thru a list of starting positions
# using a 'for' loop, with the list containing tuples of those
# positions, then creating new instances that accept those positions
# as input of their individual 'starting_ positions' state:

# starting_positions = [
#     (0, 0),
#     (-20, 0),
#     (-40, 0),
# ]

# Since we are going to be addressing each of our snake segments
# collectively, let's put those segments into an empty list above our
# previous code.

# segments = []

# ======================
# -> CREATE OUR SNAKE <-
# ======================

# for position in starting_positions:
#     new_segment = Turtle(shape="square")
#     new_segment.color("white")

# Since we don't want the segments of our snake to continuously
# draw the path they are taking (the default behavior of the
# turtle module), we need to use the .penup() method to keep this
# from happening:

# new_segment.penup()
# new_segment.goto(x=position[0], y=position[1])

# As part of our TODO 2, we are going to fill our 'segments' list
#  with list items by appending those instances to our list:

# segments.append(new_segment)

# Usually in Python when we want some function or method to continue,
# we typically use a 'while' loop.  Also, we've previously used
# variables that take a boolean value in order to support these
# 'while' loops. Let's create a new variable, is_game_on & set it to
# a boolean value of TRUE:

# In order for the game to run correctly, we need to be able to
# control our snake with key presses, so we need to call upon our
# previous lesson where we used the .listen() method & the .onkey()
# method from the turtle module to accomplish this. In order for this
# to work, we not only need to pass an attribute to indicate the key
# that we are pressing as a string (ex-"Up"), we also need to pass a
# function that will cause the listener event to be triggered::

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

is_game_on = True

while is_game_on:
    # As mentioned in the tracer() method documentation, we have to
    # invoke the .update() method under the Screen class in order for
    # it to work. We are also going to place it outside the 'for'
    # loop so that the screen updates only once all of our segments
    # have gone through the 'for' loop as opposed to including it
    # in the 'for' loop, where the behavior then would be to update
    # the screen EACH TIME a segment moved which would result in,
    # well, segmentation of the snake being visible:

    screen.update()

    # We are going to use the sleep() method within the time module
    # in order to slow down the movement of our snake segments by one
    # second. Again, as with the .update() method, we are going to
    # nest this .sleep() method within the 'while' loop but not the
    # 'for' loop so that this method applies to the "whole" of the
    # snake segments instead of each snake segment individually which
    # would cause a very slow movement. Also, since the .sleep()
    # method takes floats, we are going to create an attribute that
    # slows down the movement of our snake segments, but not to a
    # ridiculous degree. 1 second still causes very slow movement,
    # but 0.1 will do for our purposes:

    time.sleep(0.1)

    # In our 'for' loop, we are going to iterate thru each segment
    # using the range() function. We need to define the range such
    # that each instance of a snake segment will follow & "bunch up"
    # on the lead snake segment in order to properly turn. Review
    # this portion of the class to gain more clarity:

    # =====================
    # -> MAKE SNAKE MOVE <-
    # =====================

    # for seg_num in range(len(segments) - 1, 0, -1):
    #     new_x = segments[seg_num - 1].xcor()
    #     new_y = segments[seg_num - 1].ycor()
    #     segments[seg_num].goto(new_x, new_y)

    # Since the lead snake segment needs to be in continuous movement
    # in order for the game to operate correctly, we need to use the
    # .forward() method to instruct it to do so as its own state.
    # First we have to call on this particular segment from our
    # 'segments' list (using '0' to identify it since lists iterate
    # thru their items starting from '0'), then we can use the
    # .forward() method upon that particular segment:

    # segments[0].forward(20)

    # To show 'proof-of-concept' of the previous 'for' loop that is
    # iterating thru the range we specified above, we can even use
    # the .left() method to have the lead snake segment turn left &
    # watch as the other segments follow it. Let's comment out this
    # piece of code since we only wanted to use it in order to
    # confirm our previous code is working properly:

    # segments[0].left(90)

    snake.move()

screen.exitonclick()
