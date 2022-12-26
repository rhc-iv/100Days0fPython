#!/usr/bin/env python3 

# We need to import the random module before we begin
# to write our code. 
import random

# Next, since this is a virtual coin-flip, we need to 
# use the randint() function to calculate 2 random
# numbers, in our case 0 or 1.
result = random.randint(0, 1)

# Next, we need to assign 1 to 'Heads' and 0 to 'Tails'
# based on the random output, then print that output to
# the console. We can use a simple 'if/else' statement
# to accomplish this:
if result == 1:
    print("Heads")
else:
    print("Tails")