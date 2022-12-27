#!/usr/bin/env python3

# ---- DEBUG THIS CODE ----

#   year = input("Which year do you want to check?")

#   if year % 4 == 0:
#       if year % 100 == 0:
#           if year % 400 == 0:
#               print("Leap year.")
#            else:
#               print("Not leap year.")
#       else:
#           print("Leap year.")
#   else:
#       print("Not leap year.")

# In the above example, after inputting a year, the console
# returns a TypeError: not all arguments converted during
# string formatting, beginning at line 7. Looking at our input
# statement, we see that 'input' isn't wrapped in a int()
# function but it needs to be: Since we are passing on the input
# to our 'if/else' statements, which contain mathematical
# operations, the data type we should input is an integer (or,
# in this case, expressed) as a year.

year = int(input("Which year do you want to check?\n"))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")