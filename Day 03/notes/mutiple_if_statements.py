#!/usr/bin/env python3

# Previously, we learned about 'if/else' and 'elif' statements.
# We saw that they can be combined in a sort of 'if/elif/else'
# statement to check multiple conditions where if one of those
# conditions parses as TRUE, then that condition will trigger
# an action in Python.
#    if condition 1:
#        do A
#    elif condition 2:
#        do B
#    else condition 3:
#        do C
# The above code will "do" whatever the action is once the first
# boolean condition has parsed TRU then the program will stop.

# But, what if we wanted multiple actions to occur, in sequence, 
# based on mutliple TRUE boolean checks using 'if' statements?
# Well, we'd code it using this structure:
#    if condition 1:
#        do A
#    if condition 2:
#        do B
#    if condition 3:
#        do C
# We do not even have to pair the 'if' statements with an 'else'
# statment if there is no change based on a FALSE condition.
# Let's go thru this using our rollercoaster example from earlier
# in the day:

print("Welcome to the rollercoaster!!!")
height = int(input("What is your height in inches? "))

# We are going to create a new variable called 'bill', since
# the 'if' statements we are introducing will change the
# price of admission based on whether or not the rider wants
# a photo to be taken (and a dollar amount added) to the price
# of admission. Since we are making this variable before any
# price determination (be it ticket price or photo price), we
# will assign it a value of '0'.  Notice in the 'if/elif/else'
# afterward, we change the variable to the correct value (based
# on the rider's age) before we invoke the print() function.
# This is necessary to derive an initial value for the ticket
# that might changed based onn the later input.
bill = 0

if height > 58:
    print("Congratulations! You may ride on the rollercoaster!")
    age = int(input("What is your age in years? "))
    if age < 12:
      bill = 5
      print(f"The price of admission is $5.")
    elif age <= 18:
      bill = 7
      print(f"The price of admission is $7.")
    else:
      bill = 12
      print(f"The price of admission is $12.")
# Indention becomes important here.  Since the above 'if/elif/else' statement
# caculates the price of admission (and thus, the 'bill'), we want to add
# additional 'if' statments at the same level of indention since the new
# calculation (price of a photo) will also be added to the 'bill' variable.
# Also, since whether or not the rider want a photo hasn't been determined yet,
# we need to create another input choice for the rider AFTER we have checked
# their height and age:
    wants_photo = input("Do you want a photo taken? Y or N? ")

# Now, we need to add the 'if' condition based on if the answer is 'Y' because
# that input will cause a small sum of money to be added to the 'bill' which
# already has total based on the rider's age.
    if wants_photo == "Y": # Notice the double-quotes; the input is a non-converted string type.

# Take note too that there is no companion 'else' statment here since an input
# selection of 'N' adds nothing to the 'bill' variable and doesn't change it at
# all. 
      bill += 3 # This operator will add 3 to the bill vairable if the 'if' statment is TRUE
    
# Since the bill is changed once the 'if' statment is TRUE, we can print the mathematical
# operator used to change the bill variable by using an F-String on the variable.
    print(f"Your final bill is ${bill}.")

# You'll notice that there is no 'else' statment based on the previous input.
# Again, if the input above by the rider is 'N', there is no change to the bill
# that has already been calculated depending on the rider's ago, so there doesn't
# need to be an 'else' statment as the variable is unaffected.
else:
    print("Sorry, you are not tall enough to ride the rollercoaster,\ncome back later when you have grown!")

# Finally, there is an included 'rollercoaster-flowchart' image in the Day 
# 3 'notes' folder that helps to visualizeall of what we've learned about
# 'if/else', 'elif' and multiple 'if' statments.