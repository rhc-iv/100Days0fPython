#!/usr/bin/env python3

# ---- TUPLES ----

# A tuple is a data type in Python. The syntax of a tuple is very
# similar to a list in Python, but instead of square brackets, [],
# a tuple uses rounded brackets, ()

#   (1, 2, 3)

# A key difference between tuples & lists is that the data inside of
# a tuple is fixed; it cannot be altered or changed like the data
# that exists inside of a list. Once we've created a tuple, it is
# 'immutable', that is, it is permanent.

# If at some point in our code we really want to change data inside
# of a tuple, we can wrap that tuple inside of a list & it will
# undergo a TypeConversion & become mutable.

from turtle import Screen
import turtle as t
import random


tim = t.Turtle()
t.colormode(255)

# To get started with tuples, we first need to change the 'colormode'
# in the turtle module to allow us to work with RGB colors and the
# way we do this is to set the 'colormode' to '255' which is the
# upper end of the RGB range (counted up from '0') as shown above.

tim.shape("classic")
tim.pensize(15)
tim.speed("slow")


# Next, we'll delete our previous list of colors. Instead, let's
# create a new function that will allow us to use random colors in
# our program as well as to define those numbers using tuples. We'll
# create variables within our function that correspond to each of the
# primary colors (r = red, g = green, b = blue) and set the color
# range from '0' to '255', using the randint() function:


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
# The 'random_color' is now a tuple of (r, g, b):
    random_color = (r, g, b)
# We need to return the result of the tuple:
    return random_color


directions = [0, 90, 180, 270]


for _ in range(200):
    tim.forward(20)
    tim.setheading(random.choice(directions))
# The 'color' attribute now uses the random_color function that we've
    # created:
    tim.color(random_color())

screen = Screen()
screen.exitonclick()
