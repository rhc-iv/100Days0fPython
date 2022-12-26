#!/usr/bin/env python3

# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

# As with the previous exercise, let's begin
# by creating a variable (with a base value
# of '0') that we'll use to store our solution:
highest_score = 0

# Next, we will create the 'for' loop
# to arrive at our solution. Where we
# could normally apply the max() function
# to the list to derive an answer, fo the
# purposes of this exercise, we need to
# construct a 'for' loop that does the same
# thing. So, let's craft the first part of
# our 'for' loop. We will use 'score' as the
# variable name for each entry into our initial
# input that comprise the 'student_scores' list
# and make sure to end the 'for' loop statement
# with a colon (:)
for score in student_scores:

# Next, we'll use comparison logic to determine
# if each 'score' in the loop is greater than
# the value of our 'highest_score' variable, 
# which has an opening value of '0'. We can
# accomplish this by using the mathematical
# operand ">":
    if score > highest_score:

# As the loop runs, it compares each list
# entry ('score') to the value of our 
# 'highest_score' variable. Then, if that
# list item meets the condition of our mathematical
# operator (">" or 'greater than'), it will 
# replace the value of 'highest_score'. We
# express that in the code below by having 
# the 'highest_score' variable take on the value
# of the 'score' variable, but ONLY if the
# mathematical condition is me. For instance,
# we know that the initial value of 'highest_score'
# is '0' since we assigned & stored that value
# in the variable previously. Let's suppose that
# the first 'score' value (list item) is '85'.
# The 'for' loop will take that value and compare
# it to the previous value ('0' in this case)
# using the ">" operand.  Since '85' is indeed
# greater than (">") '0', it will now become the
# value of 'highest_score'. Further, what if the
# next 'score' (list item) is '79'? Well, if we
# compare '85' to '79' using the ">" operand, we
# see that '85' is the larger integer. In this
# case, '85' will remain the value of 'highest_score'
# instead of being replaced & the 'for' loop will 
# move past the value '75' and compare whatever the
# next 'score' (list item) is within the list:
        highest_score = score

# After the 'for' loop has completed all of these
# comparisons, our 'highest_score' variable will contain
# only the largest value from the 'student_scores' list
# that was created upon input. All that is left to
# do is create a print() function to return the
# solution. Since our answer is stored inside of the
# 'highest_score' variable, we can use an F-String
# within the print statement to produce the output:
print(f"The highest score in the class is: {highest_score}")