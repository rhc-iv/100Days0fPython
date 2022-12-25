#!/usr/bin/env python3

# For this exercise, we want to have the printed output switch the
# inputs between the variables a & b.  We do this by introducing a
# new variable called 'c' in this example.
# The allegory for doing this is to think of having 2 cups on a
# table.  One is a red cup filled with water, and the other is a blue
# cup filled with milk. How could we change this table setting so
# that the red cup is filled with milk and the blue cup is filled
# with water?
# The most obvious answer is that we'd introduce a third cup,
# say a green cup (the variable 'c' in this comparison) to act as
# storage for the contents of one of the cups so that we could switch
# the water & the milk between the red and blue cups. So, we create
# the variable 'c', which we pour the contents of 'a' into.  Now that
# 'a' is "empty", we can fill it with the contents of 'b'.  But this
# leaves 'b' empty, which we then fill with the contents of 'c',
# which holds the content previously held by 'a'.


# 🚨 Don't change the code below 👇
a = input("a: ")
b = input("b: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

c = a
a = b
b = c

#Write your code above this line 👆
####################################

# 🚨 Don't change the code below 👇
print("a: " + a)
print("b: " + b)