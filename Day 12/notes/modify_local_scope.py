#!/usr/bin/env python3

# Normally, we want to avoid naming global & local
# variables the same thing, but Python has a way of
# addressing this issue. Let's take the code below:

# enemies = 1

# def increase_enemies():
#     global enemies
#     enemies += 1
#     print(f"enemies inside function: {enemies}")

# increase_enemies()
# print(f"enemies outside function: {enemies}")

# Notice that we initially created a global variable
# called 'enemies'. We then created a function that
# calls on that global variable by using the keyword
# GLOBAL within our function. Now our function and
# its code block (normally operating within local
# scope) contains a globally-scoped variable that
# does not have to occur within that very function.

# Even though this is perfectly valid within Python,
# most programmers avoid modifying global variables
# within a function due to it being very fallible and
# potentially introducing bugs into our code.

# A more appropriate solution to making modifications
# to global variables is to use the RETURN keyword within
# our function, which would allow us to call that function
# anywhere in our code:

enemies = 1

def increase_enemies():
    print(f"enemies inside function: {enemies}")
    return enemies + 1

enemies = increase_enemies()
print(f"enemies outside function: {enemies}")