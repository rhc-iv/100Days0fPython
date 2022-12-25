#!/usr/bin/env python3

# Write a program that adds the digits in a 2 digit number. 
# e.g. if the input was 35, then the output should be 3 + 5 = 8

# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

# We have to do two things here in order to meet
# the exercise criteria:

#    First, we have to convert the string indicated by the
#    two_digit_number variable into an integer.  Then, we have
#    to split that integer into separate numbers using the
#    power of sub-scripting.
#    We create 2 new variables (to account for each integer in
#    the converted string 'two_digit_number'), then we use the
#    [] to tell each variable that integer of the converted
#    string to store.

new_numb_one = int(two_digit_number[0])
new_numb_two = int(two_digit_number[1])

#   After those type conversions have been made and new variables
#   have been created (along with the requisite sub-scripting), we
#   then redefine the original 'two_digit_number' variable as an
#   integer that is the sum of the two new variables (in other words,
#   the sum of the new variable integers).

two_digit_number = new_numb_one + new_numb_two

#   Finally, we print the redefined 'two_digit_number' variable
#   to the console.  It will be displayed as an integer instead
#   of delivering a TypeError because the Type Conversion has occurred
#   before the print() function has run.

print(two_digit_number)
