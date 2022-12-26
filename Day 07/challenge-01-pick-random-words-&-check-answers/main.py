#!/usr/bin/env python3

import random

# Step 1:

word_list = ["aardvark", "baboon", "camel"]

# TODO-1 - Randomly choose a word from the word_list
# and assign it to a variable called chosen_word.

#     1. Import 'random' module at the top of our code.
#     2. Create 'chosen_word' variable and apply the
#        random.choice function to it.
chosen_word = random.choice(word_list)

# TODO-2 - Ask the user to guess a letter and assign
# their answer to a variable called guess. Make guess
# lowercase.

#     1. Use the 'input'() function to print a message
#        to the console asking the user to guess a letter.
#     2. Create a new variable called 'guess' that will
#        store the user's input. Use the 'lower()' function
#        to convert the user's input to lowercase.
guess = input("Guess a letter: ").lower()

# TODO-3 - Check if the letter the user guessed (guess)
# is one of the letters in the chosen_word.

#     1. Use an 'if/else' statement to check against
#        the chosen_word for the user's input and use
#        boolean operators to derive a TRUE or FALSE
#        value.
for letter in chosen_word:
    if letter == guess:
        print("Correct!")
    else:
        print("Incorrect.")
