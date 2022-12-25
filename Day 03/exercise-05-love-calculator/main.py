#!/usr/bin/env python3

# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# First, we need to combine both inputs since the score
# relies on the TOTAL count of the letters from the phrase
# 'true love' found in both input strings. We do this by
# concatenating each string into a single string value
# stored in a new variable; in this case, 'combined_name'.
# This also ensures that Python will count each letter between
# both names only once instead of having to do the letter 
# count of each string separately, possibly increasing the 
# time for the program to run.
combined_name = name1 + name2

# Now we have to make sure that all of the input letters are
# read by Python as lowercase regardless of how the user of
# the program types their name. We use the lower() function
# to perform this conversion on the previous variable:
lower_case_string = combined_name.lower()

# After we've done the above conversion, we can use the
# count() function to count the number of letters from the
# phrase 'true love' are present in the combined_name string.
# We will do this by creating and storing separate variables
# for each letter and checking them against the lower_case_string
# variable since it has been converted:
t = lower_case_string.count("t")
r = lower_case_string.count("r")
u = lower_case_string.count("u")
e = lower_case_string.count("e")

# Now that the count() function has acted upon the converted
# variable, let's take that function's value and store it in
# a variable as well:
true = t + r + u + e

# Now let's repeat the above process but for the second word
# ('love') in the phrase:
l = lower_case_string.count("l")
o = lower_case_string.count("o")
v = lower_case_string.count("v")
e = lower_case_string.count("e")

love = l + o + v + e

# We still have to calculate a total score, which is the sum
# of the value of the letter count in 'true' and the sum of 
# the value of the letter count in 'love' expressed as a 
# two-digit number. However, the count() function produces
# integers, whereas concatenating the two values (instead of
# actually adding them together) requires that we convert both
# values into strings. We will use Type Conversion to create 
# a 'love_score' variable to accomplish this. But if we ran the
# remainder of the program, we would still get a Type Error!

#     love_score = str(true) + str(love) <--- Results in a Type Error if unchanged.

# WHY?!?!?!?
# The issue actually occurs when we begin using the logical operators,
# since we are comparing the love_score ouput (a string) to, say,
# wether or not it is equal or less than or greater than a number.
# In other words, we are trying to compare a 'str' against an
# 'int' which, like concatenation between those data types, would
# lead to a Type Error.  To fix this, we could take the 'love_score'
# variable and convert it to an integer by creating and storing another
# variable, like so:
#     converted_love_score = int(love_score)
# after the creation of the 'love_score' variable. Or, for brevity,
# we can instead convert the type inline like so:
love_score = int(str(true) + str(love))

# At this point, we could simply print the 'love_score' variable
# if we chose to:
#     print(love_score)
# But since the instructions here call for a couple of different
# reponses based on what the final love_score actually is, we will
# use our knowledge of 'if', 'else', and 'elif' statements to
# differentiate between them. Notice that we've also added parentheses
# to the logical operator statments to make the code more readable:
if (love_score < 10) or (love_score > 90):
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif (love_score >= 40) and (love_score <= 50):
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")