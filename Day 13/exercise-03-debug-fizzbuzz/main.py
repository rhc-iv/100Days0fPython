#!/usr/bin/env python3

# ---- DEBUG THE CODE ----

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print([number])

# The first issues is that any number in the FizzBuzz
# problem that is divisible by 3 *AND* 5 should result
# in printing 'FizzBuzz'. But our 1st 'if' statement
# is worded such that either part of it will parse to
# TRUE (remember: 'if' statements use boolean logic).
# Because we joined the parts of the 'if' statement
# with the 'or' keyword, 'FizzBuzz' will print in place
# of any integer divisible by 3 or 5. We need to ensure
# the 'if' statement conforms to the rules of the FizzBuzz
# game by removing the 'or' keyword and replacing it with
# the 'and' keyword.
# Even with this correction, the print statement for this
# FizzBuzz code is still not printing correctly according
# to the FizzBuzz rules. That is because after we have
# written our first 'if' statement, we need to follow it
# with additional 'elif' statements instead of more
# 'if' statements.