#!/usr/bin/env python3 

# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

# Let's first create a variable 'total_height'
# with a value of '0' and store it. NOTE: Remember
# that variable's aren't immutable; their values
# can be changed later on in the program. Our
# 'total_height' variable will be used to store
# the sum of all the input heights:
total_height = 0

# Now we will use a 'for' loop to iterate
# thru the input heights and add them to the
# 'total_height' variable. Remember that the
# name that follows 'for' is simply an inline
# variable name; it doesn't need to be enumerated
# before the 'for' loop is created. We'll use
# the variable name 'height' in this case. Also,
# we must not forget the 2 necessities of a
# 'for' loop:
#     1. adding a colon (:) to the end of the
#        loop statement, and
#     2. Indenting the code below the 'for' loop
#        so that the actions or functions are
#        executing the 'for' logic:
for height in student_heights:
    total_height += height

# To test that our 'for' loop is working as
# expected, we can follow it with a print
# statement to get the output. Since we don't
# want this statement to be acted upon by the
# 'for' loop, we'll remove the indention so
# the print() function isn't parsed as a code
# block within the 'for' loop:
print(total_height)

# Using the above mathematical operator, we have
# simulated the sum() function with the '+='
# syntax. However, we still have to figure out
# how to derive an average. Since the len() function
# is not allowed in this exercise, we have to
# figure out the total number of students whose
# heights were input, then divide our 'total_height'
# variable by that amount to get an average student
# height.

# Similar to how we created & stored a variable prior
# to our 1st 'for' loop to capture the total of heights
# from the input, we need to create a variable (with
# a base value of 0 again) that will get the total
# number of students:
number_of_students = 0

# Now we construct the next 'for' loop:
for student in student_heights:
    number_of_students += 1

# What the 'for' loop above is doing:
#     1. It is assigning the variable 'student'
#        to each item in the 'student_heights' list.
#     2. As it assigns the variable, it gives
#        that variable a value of 1, as per the
#        "=" in the "+=" operand.
#     3. Also, as it assigns the variable to the
#        list items, it adds 1 to the 'number_of_students'
#        variable, performed by the "+" in the "+="
#        operand.
# So, each input in the 'student_heights' list
# has now been given a variable name ('student'), a
# value of 1 has been assigned to each instance of
# the variable 'student' and another variable that
# we previously stored ('number_of_students') has
# collected to sum of the instance of the 'student'
# variable.

# As with our 1st 'for' loop, we can use the
# print() function (written after this 'for' loop,
# but 'outside'of it also by changing the indention
# level) so that we can see the calculated output
# of our 'for' loop to ensure it has been written
# properly:
print(number_of_students)

# Now that we've calculated the 'student_heights' total
# and the 'number_of_students' total, we simply have to
# use mathematical operators on those two numbers to arrive
# at an average height. We'll do this by creating an inline
# variable ('average_height') followed by dividing our
# 'total_height' variable by our "number_of_students"
# variable using the "/" operand. We'll also apply the
# round() function to our calculation in order to get
# an integer as our answer:
average_height = round(total_height / number_of_students)

# Lastly, we need to print our calculated average height
# to the console:
print(average_height)