#!/usr/bin/env python3

import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

from art import logo
# HINT: You can call clear() to clear the output in the console.

# Print the logo to the console to begin the program:
print(logo)

# Create an empty dictionary that will contain all of the
# bids submitted by the bidders:
bids = {}

# Create a variable, based on boolean values, that will
# determine wether all bids have been submitted or not:
bids_finished = False

# Create a function to determine who has the highest bid
# out of the dictionary of all bids submitted:
def find_highest_bidder(bidding_record):

# Create a 'highest_bid' variable with a base value of '0' since
# we will be populating it with each bid entry then using
# mathematical operations to determine which one is the
# highest (Don't forget the indention since this is part
# of the code block within our find_highest_bidder function):
    highest_bid = 0

# We need to also create a variable that will be used to 
# print the name of the winner. The winner's name will be
# expressed as a string:
    winner = ""

# We'll use a 'for' loop to iterate thru the bid entries
# and then use an 'if' statement to help determine which
# is the highest bid:
    for bidder in bidding_record:

# Here, create a variable called 'bid_amount' that is going
# to store each individual bid entry:
        bid_amount = bidding_record[bidder]

# Using an 'if' statement along with mathematical operators,
# we are going to first determine if the initial bid is
# greater than the initial 'highest_bid' variable value of '0'. If
# it is (it will be!), we will replace the '0' value with
# the new value. Then we are going to compare each successive
# bid entry against the previous bid entry. If it is GREATER
# THAN the previous bid, the value will be changed & updated
# to the new higher value. If it is LESS THAN the previous
# bid value, the value will remain untouched:
        if bid_amount > highest_bid:
            highest_bid = bid_amount

# Now we need to ensure that the bid amount for each bid
# entry (the value) is correlated with the name of the
# person making the bid (the key) within our dictionary
# that is created from the user input. In this we, we can
# derive not only the highest bid bu also the person who
# made that bid by way of using key/value pairs:
            winner = bidder

# After we have successfully derived the winning key/value
# pair, we can print the results to the console. (Notice
# that the correct indention is needed within the 
# function we're defining since the print statement is
# actually part of our 'for' loop). We'll also utilize
# F-Strings to print not only the 'winner' but also the
# 'highest bid' amount:
    print(f"The winner is {winner} with a bid of ${highest_bid}")

# Remember though that we also have a variable 'bids_finished'
# that is a boolean value; it determines if all of the bids have
# been submitted. After all, if we didn't have this variable
# included, the program would assume that the first bid input
# was the ONLY bid input & declare that entry as the winner. We
# know there will be multiple bid entries because of the fact
# that we've created an empty dictionary called 'bids'. So we
# need to use a 'while' loop to check that condition:
while not bids_finished:

# As long as 'bids_finished' has a value of FALSE, we need to 
# make sure that bidders are presented with the ability to input
# their bids to the program via the console:

    name = input("What is your name? ")
    price = int(input("What is your bid? $"))

# Here, lets create a list of these entries so that iterating
# thru the list works properly:
    bids[name] = price

# Let's create a variable that will store input as to
# whether or not there are any successive bid entries that
# need to be made. Let's also create a newline at the end
# of this input to make the input answer more readable:
    should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")

# As ever, if our input consists of multiple possibilities,
# we can use 'if/else' statements to define what the outcome
# should be based on those inputs. Also remember that these
# statements should use mathematical operands to check their
# conditions:
    if should_continue == "no":

# Based on an input of 'no' (as an answer to the
# 'should_continue' variable above), we can cease
# the bidding at this point, therefore triggering
# the 'bids_finished' variable to a boolean value
# of TRUE. (Again, pay attention to indentation):
        bidding_finished = True

# Once bidding ends, we need our 'find_highest_bidder'
# function to act upon the input saved to the 'bids'
# variable:
        find_highest_bidder(bids)

# If the 'should_continue' state is True, predicated
# on an input answer of 'yes', then we need to clear
# the console (using the import os & clear definition
# created at the top of our code). We can accomplish 
# this with an 'elif' statement:
    elif should_continue == "yes":
        clear()
