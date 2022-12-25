# 🚨 Don't change the code below 👇
number = int(input("Which number do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# Create a variable from the input that applies the
# Modulo Operator to that input.
answer = number % 2

# Write an 'if/else' statement that produces a boolean value
# for whether the input (after Modulo) is even or odd.
if answer == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")

# The 'if' statement can also be written inline without
# constructing a new variable like so:
#   if number % 2 == 0: