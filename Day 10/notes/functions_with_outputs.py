#!/usr/bin/env python3

# ---- Functions With Outputs ----

#     def my_function():
#         result = 3 * 2

# If we define a function as above, where we create
# a variable in the code block of the function, we
# can use the function output keyword 'return' 
# combined with that variable to output the value
# of that variable to the console:

#         return result

# Notice that the indention of the return statement
# remains within the code block of our defined function
# so that the output is part of the definition itself.

# The output of the function can also be saved & stored
# for later use in our program by assigning the function
# itself to a variable after the return operation has
# run within the called function:

#     output = my_function()

# Let's go ahead & create some functions with outputs:
def format_name(f_name, l_name):
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
#   print(f"{formatted_f_name} {formatted_l_name}")

# So we've created 2 variables within the 'format_name'
# function that we are defining: 'formatted_f_name' &
# 'formatted_l_name', both of which will have output
# due to the TitleCase conversion applied to the arguments
# passed to the 'f_name' key & the 'l_name' key. Further,
# we went ahead and added a print statement with 
# F-Strings (using our variable names) to print the
# output of the function call to the console.

# Let's skip the print statement & instead use the
# 'return' keyword on our F-String:
    return f"{formatted_f_name} {formatted_l_name}"

# Now that the 'return' keyword is the trigger for
# our F-String, we can create a print statement
# that calls our function & it will output the
# return statement along with the data that has
# been parsed thru the title() function:

print(format_name("robert", "CARR"))