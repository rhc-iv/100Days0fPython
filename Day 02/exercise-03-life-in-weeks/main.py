#!/usr/bin/env python3

# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

# First, we need to convert the input 'age' (expressed in years) from
# a string (the initial input) to an integer.

years = 90 - int(age)

# Next, we need to define & store variables for each of the expected
# outputs: days, weeks, & months. We use the round() function to
# ensure that the only output from Python is integers.

days = round(years * 365)
weeks = round(years * 52)
months = round(years * 12)

# Finally, we use an F-String to deliver the output: print(f"You have
# {days} days, {weeks} weeks, and {months} months left\until you
# reach the ripe old age of 90! Wow!   Amazing!")

# BUT WAIT!  Why is the above code commented out? Well, if we
# un-commented the above code, the program would still work and the
# output would be correct. But, F-Strings (like functions or
# mathematical operations) can also be stored as variables. Taking
# the F-String in the code above and storing it as a variable will
# allow our print() function to work on the variable and the code
# will be easier to read and likely easier to understand.

message = f"You have {days} days, {weeks} weeks, and {months} months " \
          f"left\nuntil you reach the ripe old age of 90! Wow! Amazing!"

# Now that the F-String is defined & stored, we simply print it to
# the console by acting on the variable instead of the entire F-String!

print(message)
