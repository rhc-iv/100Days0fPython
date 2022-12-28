from turtle import Turtle, Screen

# We need to import the random module in order to vary the speeds of
# the turtle objects participating in our race. All imports precede
# any lines of code in Python so they appear at the beginning of .py
# files:

import random

# ---- Build a Turtle Race game using the turtle module ----

screen = Screen()

# We need to create a variable, 'is_race_on' (boolean value) to
# indicate to our program when the race begins & when the race ends.
# This variable will also act as a trigger for other functions in our
# code, particularly to begin randomizing the pace of each turtle
# instance. We will store a value of FALSE in this variable and use
# the 'user_bet' input to trigger a switch to a value of TRUE:

is_race_on = False

# Use the .setup method to create a program-defined screen size for
# our Turtle Race game. .setup takes integers or float values as
# parameters. Also, to make our code have more clarity, we will use
# keyword arguments instead of positional arguments for this purpose:

screen.setup(width=500, height=400)

# Next, we will use the .textinput method from our turtle module to
# create a pop-up window (within our main window) that will require
# some input from the user. For our purposes, we will be asking the
# user to make a 'bid' on which turtle object they think will win the
# game. The .textinput method takes, as parameters, strings that will
# indicate the title of the pop-up window & a prompt for the user to
# read & react to. Again, we will keep our code consistent & clear by
# using keyword arguments instead of positional arguments.
# Since we plan on storing the user's input, we will create a new
# variable called 'user_bet' so that we can capture & store this
# input from the user to call later on in our code:

user_bet = screen.textinput(
    title="Make your bet: ",
    prompt="Which turtle will win the race? Enter a color: ",
)


# Since we know we are going to be using multiple turtle instances
# during our race, let's create a list that contains the colors
# that we want our turtle objects to use during the race:

colors = [
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "indigo",
    "violet",
]

# We also know that in addition to multiple colors, our turtle
# objects are also going to have multiple starting positions. Because
# they will all start from the same x-position, we need to somehow
# assign only different y-positions. To do this, we can create
# another list of y-positions similar to our 'colors'
# dictionary created above (using a 'gap' between each object of 40):

y_positions = [
    -110,
    -70,
    -30,
    10,
    50,
    90,
    130,
]

# We are also going to create an empty list, 'all_turtles', that will
# append each individual turtle object as a list item as they are
# created:

all_turtles = []


# Next we want to create all of our turtle objects (instances) for
# the race. Let's use a 'for' loop combined with our 'colors' library
# and our 'y_positions' library created above to accomplish this:

for turtle_index in range(0, 7):

    # Next, let's indicate the attributes & methods that will be endemic
    # to all of the turtle objects:
    # The Turtle() class actually accepts an __init__ parameter of
    # shape, so instead of using the .shape method for each turtle
    # object we create, we can just set that upon initialization of
    # the program in the Turtle() class itself. Since we aren't
    # interested in our turtle objects drawing their paths (as is the
    # default behavior for turtle objects), we also use the .penup()
    # attribute to ensure that each instance of our racing turtles
    # doesn't marks its individual path. Finally, we are going to
    # select the object 'tim' and Refactor it from within PyCharm to
    # a new name of 'new_turtle':

    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()

    # After the user input, we want our turtles to begin at a 'starting
    # line' at the left edge of the screen. Because there will be more
    # than one turtle object competing in this race, adding the
    # .backward method wouldn't make sense because all of the objects
    # would overlap each other at the beginning of the race. Instead,
    # we can use the .goto method in the turtle module to set
    # starting positions for each turtle object that will participate
    # in the race (using keyword arguments as in our other code).
    # REMEMBER: because we previously used the .setup method to
    # define our screen size, we need to think of our screen in terms
    # of a grid. That is, the center of the screen would be our x=0,
    # y=0 coordinates. From this, we can work out what positions our
    # turtle objects will need for their .goto method parameters in
    # order to line them up along a starting position. Since all of
    # the instances of our turtles will have the same x-position at
    # start, we are going to tap into our 'y_positions' dictionary to
    # assign different y-values for each of the turtle objects
    # Likewise, we are going to use the .color method in the turtle
    # module to loop thru our 'colors' dictionary to get the same
    # effect of assigning each objects its own color value:

    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_positions[turtle_index])

    # We are also going to use the .append() to put each new turtle
    # object into our 'all_turtles' list:

    all_turtles.append(new_turtle)

# Remember our 'is_race_on' variable created earlier? We are going to
# use an 'if/else' statement in order to switch between boolean
# values for it. Since we defined & stored it with a value of FALSE,
# let's use an opening 'if' statement to check if our 'user_bet'
# function has been called & if it has, switch the value of
# 'is_race_on' to TRUE:

if user_bet:
    is_race_on = True

# Next, if 'is_race_on' DOES have a value of TRUE, we can then
# trigger the race to occur while that condition remains the same:

while is_race_on:

    # Since all of our turtle object creations have been appended to
    # our 'all_turtles' list, we are going to iterate thru them using
    # a 'for' loop while the race is ongoing:

    for turtle in all_turtles:

        # We need to indicate what the position is for the end of the
        # race. We know that, from the 0,0 coordinates (the middle of
        # the screen & with a width of 500), that the right side of
        # the screen from the middle is half of our window width. So,
        # in this case, 250. But, the default 'size' of a turtle
        # object on the screen is 40. Since we want the race to end
        # before any of our turtle instances go off-screen, we need
        # to subtract half of the size of the turtle from 250 to get
        # an end point. That leaves us with 230. Also, because all
        # turtle instances have a true point on the window that is in
        # the middle of the rendered graphic, we only had to subtract
        # half of its 'size' from the right-half distance instead of
        # the full 40. We can now tap into the .xcor() method in the
        # turtle module to create a condition for each of the turtle
        # instances to stop once that x-coordinate has reached 230.
        # If the object has not yet hit an x-position of 230, then it
        # should still call the .forward method until it does. We can
        # do this thru the use of an 'if/else' statement:

        if turtle.xcor() > 230:

            # First, let's create a trigger to end the race. We will
            # tie the 'is_race_on' variable to a FALSE value since
            # our 'if' statement is for a condition where one of our
            # turtle instances has reached the 'finish line'.

            is_race_on = False

            # Since the 'if' statement is predicated on one of our
            # turtle objects reaching the 'end' of the race,
            # we'll create a variable that stores that information:

            winning_color = turtle.pencolor()

            # And we will nest another 'if' statement to check &
            # see if our winning condition (winning_color) matches
            # the 'user_bet' input from the start of the game. Also
            # we will print out if the user has won based on our 'if'
            # statement or if they've lost (based on a follow-on
            # 'else' statement):

            if winning_color == user_bet:
                print(
                    f"You've won! The {winning_color} "
                    f"turtle has won the race!"
                )
            else:
                print(
                    f"You've lost! The {winning_color} "
                    f"turtle has won the race!"
                )

        # Within our 'while' loop, we can use the randint() function
        # from our imported random module to generate random 'speeds'
        # for each of our turtle objects & move them accordingly
        # across the window or 'race map'. This is also going to be
        # stored to a variable called 'rand_distance':

        rand_distance = random.randint(0, 10)

        # This 'rand_distance' variable needs to be passed to the
        # .forward method within the turtle module so that our turtle
        # objects are getting the instructions & moving a random
        # distance over the length of the race:

        turtle.forward(rand_distance)


screen.exitonclick()
