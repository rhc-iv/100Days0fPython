#!/usr/bin/env python3

#Write your code below this row 👇

# As with all of our previous exercises, we
# are going to create a new variable with a
# value of '0' which will store the value that
# is derived from our 'for' loop:
even_total = 0

# Next, we only want to add the 'even' numbers
# in our range (between '1' and '100'). We also 
# know that we could add a 'step' for our 'for'
# loop to skip all of the 'odd' numbers. But if
# we add '2' as our 'step' and then start at '1'
# (the beginning of our range), we will actually
# end up with a collection of 'odd' numbers that
# will be added to our total too. But, since we
# have only been presented with a requirement for
# this exercise to add all of the 'even' numbers
# between '1' and '100', there's no additional
# requirement that states how we must define the
# range. REMEMBER: we just need to add together
# all of the 'even' numbers between '1' and '100'.
# That's all! What if we changed the beginning of
# our range from '1' to '2'? Since we know that
# '1' is not an even number, it's perfectly fine
# to exclude it since it won't be added to the
# total.  Also, if we use '2' as our step and
# '2' as the beginning of our range, we know that
# each iteration of the 'for' loop (guided by the
# 'step' integer in our range) will land on each
# successive 'even' number. If we use our "+="
# operand within this newly-constructed 'for'
# loop, then we can also ensure that our initial
# variable ('even_total) will not only add the
# next 'even' number in our range to its value,
# but it will do so until the 'for' loop has
# completed going thru our defined range!

# Here is our solution:
for even_numbers in range(2, 101, 2):
    even_total += even_numbers

# Remember to see the output in the console, 
# we use the print() function moved back to
# the original indentation if we only want
# to see the output in its final form. If we
# keep the print statement indented beneath
# the 'for' loop, it will be read by Python
# as a code block WITHIN the 'for' loop and
# will print each iterable calculation that
# the 'for' loop is producing.
print(even_total)