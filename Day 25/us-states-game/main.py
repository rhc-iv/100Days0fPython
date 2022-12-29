#!/usr/bin/env python3

import turtle

# TODO 1: Import pandas module
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

# TODO 2: Import the included .csv file into Python via the pandas
#  module and save the DataFrame as a variable:

data = pandas.read_csv("50_states.csv")

# TODO 3: We need to create an "all_states" list that we'll use later
# to check the user's answer against this list:

all_states = data.state.to_list()

# TODO 4: Now we will create a list called "guessed_states" that will
# take the user's input and append it into an empty list that we'll
# use to keep track of all the user's answers and use that list to
# determine if the game is over or not:

guessed_states = []

# TODO 6: Using a 'while' loop, we are going to set game conditions
# based on the "guessed_states" list. Since we know that there are 50
# states on the list, we'll use the len() function to determine if
# the user has guessed all of the states by checking the number of
# items in the "guessed_states" list versus the number of items in
# the "all_states" list:

while len(guessed_states) < 50:

    # TODO 5: Use the "input" function to get the user's answer
    #  and append it to the list "guessed_states". Also, we are going
    #  to use the title() function in order to take the user's input
    #  and convert it to TitleCase so that if the input is lowercase,
    #  it will still match the states on our list if spelled
    #  correctly regardless of whether or not the input is capitalized:

    answer_state = screen.textinput(
        title=f"{len(guessed_states)}/50 States Correct",
        prompt="What's another state's name?",
    ).title()

    # We need to create an 'if' statement that accepts a keyword
    # input that will cause the game to exit then save all of the
    # game data to a .csv file. We are going to use the "break"
    # keyword to do this:

    if answer_state == "Exit":

        # We can clean up our code below & save a few lines if we
        # apply List Comprehension that is discussed in the Day 26
        # Course Section:

        missing_states = [state for state in all_states if state
            not in guessed_states]

        # for state in all_states:
        #     if state not in guessed_states:
        #         missing_states.append(state)

        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

# TODO 4: We are going to use an 'if' statement to check the user's
# answer input against our list of known states. We are only able to
# use the "in" keyword because we are checking against a list; we
# would not be able to use it if we were checking against a variable:

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

# Lastly we want to save & convert all of our game information into
# its own .csv file:
