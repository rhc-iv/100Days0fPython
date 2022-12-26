#!/usr/bin/env python3

# While examples of Randomization (or, Randomness) are
# fairly simple to find in everyday life, computers by
# their very nature are 'Deterministic', that is, they
# perform calculations & operations in a repeatable
# manner. Python uses the 'Mersenne Twister' which is
# a pseudo-random number generator. We don't necessarily
# have to know everything about this particular algorithm;
# in fact, we don't have to know anything about it at all.
# But, as a Python programmer, it is important to know how
# to have this algorithm available to us within our own 
# applications.
# The way that Python does this is by relying on a 'module',
# which is a type of program written for a specific purpose
# that we can 'import' into Python for use in our applications
# and other coding endeavors. These modules, if we are using
# them in a particular app, need to be imported ahead of the
# rest of our code, like so:
import random

# Once the module has been imported, we have access to
# any function or operation that the module provides within
# Python. A good place to start with modules is askpython.com
# When we search for the 'Random module' on that website, we
# are presented not only with an introduction to the module,
# but we also have examples of the module's functions explained
# as well along with examples.  One of those functions is the
# randint() function.  This function takes all numbers within
# a range between 2 numbers (written within the parentheses
# and separated by a comma) and returns a random number
# within that range & can include both input integers at the
# ends of the range. See this example below:
random_integer = random.randint(1, 10)

print(random_integer)

# Let's look at the function that will print a random number,
# but expressed as a float instead of an integer. The
# random() function (which takes no arguments) will simply
# print a random float between 0.0 and 1.0 (but not 
# including 1.0 itself) whenever it is invoked in our 
# code. See below:
random_float = random.random()

print(random_float)

# The first 'think-about-it-and-try' exercise in this
# class section asks how we could generate a random
# number, expressed as a float, between 0 and 5. Since
# we already know that the random() function returns
# outputs between 0.0 and 1.0, we could use a mathematical
# operator (in this case, multiplication) to increase
# the range of the returned value of the random() function.
# Let's give it a try!
random_range = random_float * 5.0

print(random_range)

# In our previous class, we created a Love Score calculator
# that used the letter count totals from 2 name inputs to form
# and integer which was the 'love score' output. Since that
# program wasn't based on actual science, we could instead
# just use the randint() function, along with an F-String
# to output a score like so:
love_score = random.randint(1, 100)

print(f"Your love score is {love_score}.")