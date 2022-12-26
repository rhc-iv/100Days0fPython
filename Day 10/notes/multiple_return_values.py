#!/usr/bin/env python3

# In Python, the 'return' keyword in a function's
# code block acts as an escape sequence: that is, it
# will return the output of the function while stopping
# the function as well. Any code like, say, a print statement
# that is written within the same indentation level as the
# 'return' keyword AND comes after the 'return' keyword will
# be ignored.

# But Python allows for use to use more than one 'return'
# keyword within our defined functions. One way to accomplish this
# is to make all 'return' keywords in the function definition
# indented before the final use of the 'return' keyword.

# Let's use the previous example in our introduction to the
# 'return' keyword to illustrate this:
def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs."
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f"Result: {formatted_f_name} {formatted_l_name}"

print(format_name(input("What is your first name? "), 
input("What is your last name? ")))

# The first 'return' statement in our function above
# acts as an escape sequence and, since it is empty due to
# the condition of the 'if' statement, will print "None"
# to the console if the 'if' statement is satisfied. But this
# might not make sense to the user or developer, so we can
# use that conditional return statement to give an output
# that makes more sense in the form of the string after it.