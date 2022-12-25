#!/usr/bin/env python3

# To give a 'real world' example of how logical operators work,
# we are going to incorporate them into our previous rollercoaster
# code. The owner of the rollercoaster has decided that all riders
# who meet the requirements to rid and who are between the ages of
# 45 and 55 will be allowed to ride for free due to that age range
# possibly being effected by a mid-life crisis. 

# Here is the last rollercoaster program we wrote:
print("Welcome to the rollercoaster!!!")
height = int(input("What is your height in inches? "))

if height > 58:
    print("Congratulations! You may ride on the rollercoaster!")
    age = int(input("What is your age in years? "))
    if age < 12:
      print("The price of admission is $5.")
    elif age <= 18:
      print("The price of admission is $7.")
# At this point we need to create another age category that is
# inline with the owner's wishes. To do this, we'll create another
# 'elif' statment but use the logical operator 'and' to create
# the new age range AND to elicit an output for elible riders
# about the free ride:
    elif age >= 45 and age <= 55:
      print("Everything is going to be ok. Have a free ride on us!") # Pretty easy, huh?
    else:
      print("The price of admission is $12.")
else:
    print("Sorry, you are not tall enough to ride the rollercoaster,\ncome back later when you have grown!")