#!/usr/bin/env python3

# Review:
# Create a function called greet().
# Write 3 print statements inside the function.
# Call the greet() function and run your code.
# def greet():
#     print("Hello")
#     print("World!")
#     print("Goodbye, World!")


# greet()

# Functions with inputs allow us to create a
# variable within our function, then later pass
# on data to that variable when we call our
# function.

#     def my_function(variable):
#         do_something_with(variable)
#         do_something_different_with(variable)
#
#     my_function(data_goes_here)

# In the above example, whatever data we add
# when we call our function will be stored as
# a variable in the function.

# Let's create a function that allows for input:
def greet_with_name(name):  # <-- 'name' is the PARAMETER
    print(f"Hello {name}")
    print(f"How are you doing {name}?")


greet_with_name("Robert")  # <-- 'Robert' is the ARGUMENT
