#!/usr/bin/env python3

#   number = int(input("Which number do you want to check?\n"))

#   if number % 2 = 0:
#       print("This is an even number.")
#   else:
#       print("This is an odd number.")

# ---- DEBUG THE CODE ABOVE ----

# When I run the code in my terminal, I get a SyntaxError
# : invalid syntax that points to line 5 & emphasizes the
# "=" operand. The reason is because the "=" operand is used
# to define variables & lists.  Since the math function that
# I want to access in my 'if' statement is "equal to", then
# I need to correct the operand to "==":

number = int(input("Which number do you want to check?\n"))

if number % 2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")