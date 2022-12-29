#!/usr/bin/env python3

from turtle import Screen

# We will import the 'time' module to have access to methods that
# will allow us to slow down the 'snake segments' as the game is
# being played on the screen:

import time

# Since we have created a separate snake.py file, which will act as
# our Snake class, we have to import it as well:

from snake import Snake

# Like the Snake class above, we need to create an import statement
# for our Food class:

from food import Food

# The first thing we're going to do is to create a new screen which
# is basically the window in which the game will take place. We are
# going to use the .setup() method to define the size of the screen (
# using keyword arguments), we're going to use the .bgcolor() method
# to make the background of the screen black and we are going to use
# the .title() method to give a title to the screen. As ever, at the
# bottom of our code, we are also going to call the .exitonclick()
# method so that the screen remains open until we click it with our
# mouse:

from scoreboard import Scoreboard

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

# Likewise, we're going to import our Food class and, similar to our
# Snake class, it will trigger the __init__ of our food.py file and
# all of the attributes/methods (and appearances/behaviors due to it
# inheriting from the superclass) in-game:

food = Food()

# Here we'll create our Scoreboard object from the Scoreboard class
# that we've made in our scoreboard.py file:

scoreboard = Scoreboard()

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

    # Now we need to create a way for the Snake to detect a collision
    # with the Food object, which will replicate the Snake "eating"
    # the Food & which will also trigger the portion of our __init__
    # method in the Food class to have another piece of food appear
    # randomly on our screen. The turtle module has a method called
    # distance() that returns the turtle instance's distance from an
    # x/y coordinate or even another turtle instance. We can take our
    # lead snake segment (snake.head) and use the .distance() method
    # to determine its proximity to the Food object. We will also
    # call this method using an 'if' statement:

    if snake.head.distance(food) < 15:
        # When the lead snake segment collides with the Food object,
        # we are going to have that Food object refresh its location by
        # calling on the refresh() method that we created in the food.py
        # file:

        food.refresh()

        # Since we need to "grow" the Snake object each time it
        # "eats" a piece of food, we're going to call on the extend()
        # method that we created within our Snake class (via the
        # snake.py file) so that a new snake segment gets added under
        # these conditions:

        snake.extend()

        # Now let's access the increase_score function in our
        # scoreboard.py file to tell our game to update the score
        # anytime the lead snake segment collides with a piece of the
        # food:

        scoreboard.increase_score()

    # We need some way to tell the game when our Snake object hits
    # the "wall" or the sides of the screen. In the game rules for
    # Snake, hitting the wall signifies a "Game Over"-type of
    # condition. We know that our screen is 600 x 600. We also know
    # that if we split the screen upon the x- and y-axis, then the
    # distance from the center of the screen (0,0) is 300 (or -300)
    # in any direction. We also know from our previous code where we
    # created a random generation of the Food object that it will not
    # appear anywhere beyond (270, -270) on our screen. We also know
    # that our lead snake segment, the head, is 20 x 20 pixels in
    # size. So, if we subtract the size of that segment from the
    # total distance along the x- & y-axis (from the center of the
    # screen), we get 280.  Graphically, at 280 (or -280) the Snake
    # object would appear to be "touching" the wall, which according
    # to the game rules, means the game should end. We are going to
    # use an 'if' statement to determine what happens when our Snake
    # object hits the wall (that is, this condition should trigger
    # the end of the game). To allow for this, we'll use the ">"
    # operand comparing the Snake object's current xcor() and ycor()
    # values against that (280, -280) barrier:

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or \
        snake.head.ycor() > 280 or snake.head.ycor() < -280:
        # We'll use these above 'if' conditions to trigger a change
        # in our 'is_game_on' variable from TRUE to FALSE:
        # Now we want the Scoreboard object to trigger the sequence
        # that alerts the user that the game is over:
        scoreboard.reset_game()

    # In addition to the "Game Over" condition that occurs when our
    # Snake object collides with the wall, we also need another
    # similar condition that triggers whenever our Snake object
    # collides with its own tail. We'll begin this process with a
    # 'for' loop so that our game is constantly iterating thru our
    # Snake object segments to check whether or not any collision is
    # actually occurring. But we're actually going to do this instead
    # thru what we learned in our slicing.py file contained in the
    # Notes directory for this project. We're going to slice the
    # segments of our snake, ignoring the lead snake head. Our
    # initial slice integer is going to start at the 1 list item
    # position, which is actually the 2nd list item because lists
    # enumerate starting at 0. Therefore, the first list item,
    # our lead snake segment, will be skipped in the slice:

    for segment in snake.segments[1:]:

        # Now we need to exclude checking against the lead snake
        # segment, or the head in this case, because it will always be
        # less than the minimum distance that we are going to use to
        # check for a collision. We'll use an 'if/elif' set of
        # statements to accomplish this:

        # The 'if' statement will check if the currently iterated
        # segment is equal to the lead snake segment and, if it is,
        # do nothing in response via the 'pass' keyword. We are going
        # to comment out this code though, instead using a list slice
        # above to do this same thing:

        # if segment == snake.head:
        #    pass

        # Now we'll invoke the 'elif' statement to check all of the
        # other Snake object segments against a defined distance & if
        # that condition is met, we'll trigger the 'game_is_on' value
        # switch from TRUE to FALSE and we'll trigger the 'game_over'
        # function that we created in our Scoreboard class. Last,
        # we're actually going to change the 'elif' statement to an
        # 'if' statement because we've added a slice to our list as
        # shown in the 'for' loop above. In this way, our if
        # statement will still work correctly:

        if snake.head.distance(segment) < 10:
            scoreboard.reset_game()

screen.exitonclick()
