#!/usr/bin/env python3

############ DEBUGGING#####################

# #Print is Your Friend
# Using the print() function, our output in the code
# below shows '0' in the terminal, although our calculation
# after our inputs is supposed to multiply the pages by 
# the word_per_page. Assuming that both are positive numbers,
# the output should be greater than '0' each time we run
# the code.
# If we replace 'total_words' in our print statement with 
# the 'pages' variable, the output in our console matches our
# input. But if we do the same with our 'word_per_page'
# variable, the output again shows '0', so we know that there
# is an issue with defining & storing that variable. If we
# look carefully at the input function for 'word_per_page',
# we'll see that our operand is incorrect. Instead of using
# "=", which is how we define variables, we've instead used
# "==" which is used as a mathematical operator. In this 
# case, the variable is defined incorrectly.

#   pages = 0
#   word_per_page = 0
#   pages = int(input("Number of pages: "))
#   word_per_page == int(input("Number of words per page: "))
#   total_words = pages * word_per_page
#   print(word_per_page)

# Let's correct the operand in our input function for
# the 'word_per_page':

pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page = int(input("Number of words per page: "))
total_words = pages * word_per_page
print(total_words)