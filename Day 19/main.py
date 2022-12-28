#!/usr/bin/env python3

from turtle import Turtle, Screen


tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)

# The listen() function in the 'turtle' module tells the 'screen'
# object to listen using whatever functions we used from the module
# that act as event listeners:


screen.listen()


# The below function from the 'turtle' module is a type of event
# listener. It accepts, as parameter, a 'key'(the physical key on our
# keyboard that will trigger the event) and a 'fun'(the function that
# should be called when the event is fired).
# What we've essentially got in the code below is a function that
# acts as an input.
# NOTE: Whenever we use a function to be passed as an argument (as
# below) we don't add the function's parentheses in the argument:
screen.onkey(key="space", fun=move_forwards)
screen.exitonclick()

# The '.onkey()' function above is what's known in Python as a Higher
# Order Function; that is, it can accept other functions as inputs &
# those functions as inputs will work within the Higher Order
# Function. In Python, HOFs are pretty commonly used. They are
# especially useful in combination with event listeners when we need
# that even to trigger a particular function. NOTE: when using
# functions that we haven't created ourselves, it is best practice
# when working with parameters to use keyword arguments instead of
# positional arguments.

