#!/usr/bin/env python3 

# Create a greeting for the Band Name Generator App.

print("Welcome, you absolute nerd!\n""This is the Band Name Generator "
      "App\n")

# Ask for input for the first section of the app, ensure the input
# begins on a newline, and save that input as a variable.

body = input("What part of your body most embarrasses you?\n")

# In the second section, repeat the steps from the previous comment,
# but for the next bit of input solicited from the user.

print("")
pet = input("What would be the plural form of your favorite pet's"
            " name?\n")

# Print a string for dramatic effect before the app's result:

print("")
print("Your brand-spankin'-new band name is...\n")

# Use the '+' operand to combine both sets of input (variables) to
# generate a result in the app.  Be sure to include a string in
# between the variables for a multi-word result and add a string of
# exclamation points at the end to round out the dramatic effect!

print(body + " " + pet + "!!!")
