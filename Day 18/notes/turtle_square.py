#!/usr/bin/env python3

from turtle import Turtle, Screen

tim = Turtle()
tim.shape("classic")
tim.color("LightSeaGreen")
tim.pencolor("IndianRed1")

# Now that we have a few of the turtle attributes entered in, we need
# to make the turtle complete a square. Below we see perfectly valid
# code that would give us the result we seek:

#   timmy_the_turtle.left(90)
#   timmy_the_turtle.speed(3)
#   timmy_the_turtle.forward(100)
#   timmy_the_turtle.left(90)
#   timmy_the_turtle.speed(3)
#   timmy_the_turtle.forward(100)
#   timmy_the_turtle.left(90)
#   timmy_the_turtle.speed(3)
#   timmy_the_turtle.forward(100)
#   timmy_the_turtle.left(90)
#   timmy_the_turtle.speed(3)
#   timmy_the_turtle.forward(100)

# The issue above, even though it works, is that it's redundant & can
# be cleaned up a bit without typing or copy & pasting all of the
# repeat lines of code. Remember how 'for' loops can assist us with
# repetition. Let's try this:

for _ in range(4):
    tim.speed(1)
    tim.forward(100)
    tim.left(90)

# In PyCharm, if we right-click on a variable name (
# 'timmy_the_turtle' in this example), we can select
# 'Refactor'-->'Rename' to change that variable's name. You'll notice
# that 'timmy_the_turtle' is now 'tim' thanks to refactoring the
# variable name thru the right-click menu.


screen = Screen()
screen.exitonclick()
